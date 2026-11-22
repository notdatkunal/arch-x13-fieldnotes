#!/usr/bin/env python3
"""Compile Markdown posts in posts/*.md into a static HTML blog under _site/."""

from __future__ import annotations

import datetime as dt
import html
import re
import shutil
from email.utils import format_datetime
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
TEMPLATES_DIR = ROOT / "templates"
ASSETS_DIR = ROOT / "assets"
OUT_DIR = ROOT / "_site"

SITE_TITLE = "Kunal's Blog"
SITE_HANDLE = "@notdatkunal"
SITE_URL = "https://notdatkunal.github.io"
SITE_DESCRIPTION = (
    "Personal blog by Kunal (@notdatkunal) — notes on Linux experiments, "
    "developer tooling, hardware tinkering, and whatever else I'm exploring."
)


def parse_frontmatter(raw: str) -> tuple[dict[str, object], str]:
    """Extract simple YAML-style key/value frontmatter and return (meta, body)."""
    if not raw.startswith("---\n"):
        return {}, raw
    end = raw.find("\n---\n", 4)
    if end == -1:
        return {}, raw

    header = raw[4:end]
    body = raw[end + 5 :]
    meta: dict[str, object] = {}

    for line in header.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = [item.strip().strip("'\"") for item in val[1:-1].split(",")]
            meta[key] = [item for item in items if item]
        else:
            meta[key] = val.strip("'\"")
    return meta, body


def slug_from_filename(path: Path) -> str:
    """Turn '2026-11-22-my-post.md' into 'my-post'."""
    stem = path.stem
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)


def format_date(date_str: str) -> tuple[dt.date, str]:
    """Parse YYYY-MM-DD and return (date_obj, formatted_display)."""
    parsed = dt.date.fromisoformat(date_str)
    return parsed, parsed.strftime("%b %d, %Y")


def estimate_reading_time(text: str) -> int:
    """Estimate reading time in minutes at ~200 words/min."""
    words = len(re.findall(r"\w+", text))
    return max(1, round(words / 200))


def render_template(template_name: str, **context: str) -> str:
    """Substitute {{key}} placeholders in a template file."""
    tpl = (TEMPLATES_DIR / template_name).read_text(encoding="utf-8")
    for key, value in context.items():
        tpl = tpl.replace(f"{{{{{key}}}}}", value)
    return tpl


def build_tag_badges(tags: list[str], clickable: bool = False) -> str:
    """Render HTML pills for a post's tags."""
    out = []
    for tag in tags:
        safe = html.escape(tag)
        if clickable:
            out.append(f'<button class="tag-pill" type="button" data-tag="{safe}">#{safe}</button>')
        else:
            out.append(f'<span class="tag-pill">#{safe}</span>')
    return "\n".join(out)


def build_rss(posts: list[dict[str, object]]) -> str:
    """Generate a minimal RSS 2.0 feed for the blog."""
    items_xml = []
    for post in posts:
        post_url = f"{SITE_URL}/posts/{post['slug']}/"
        pub_dt = dt.datetime.combine(post["date_obj"], dt.time(12, 0), tzinfo=dt.timezone.utc)
        items_xml.append(
            f"""    <item>
      <title>{html.escape(str(post["title"]))}</title>
      <link>{post_url}</link>
      <guid>{post_url}</guid>
      <pubDate>{format_datetime(pub_dt)}</pubDate>
      <description>{html.escape(str(post["summary"]))}</description>
    </item>"""
        )

    now = format_datetime(dt.datetime.now(dt.timezone.utc))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{html.escape(SITE_TITLE)}</title>
    <link>{SITE_URL}/</link>
    <description>{html.escape(SITE_DESCRIPTION)}</description>
    <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(items_xml)}
  </channel>
</rss>
"""


def main() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    shutil.copytree(ASSETS_DIR, OUT_DIR / "assets")
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "sane_lists", "toc"],
        extension_configs={"toc": {"permalink": False}},
    )

    posts: list[dict[str, object]] = []
    for md_path in sorted(POSTS_DIR.glob("*.md")):
        raw = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        if str(meta.get("draft", "")).lower() == "true":
            continue

        title = str(meta.get("title") or md_path.stem)
        date_str = str(meta.get("date") or "2026-01-01")
        date_obj, date_human = format_date(date_str)
        summary = str(meta.get("summary") or "")
        tags = list(meta.get("tags") or [])
        slug = str(meta.get("slug") or slug_from_filename(md_path))
        minutes = estimate_reading_time(body)

        md.reset()
        content_html = md.convert(body)

        posts.append(
            {
                "title": title,
                "date_str": date_str,
                "date_obj": date_obj,
                "date_human": date_human,
                "summary": summary,
                "tags": tags,
                "slug": slug,
                "minutes": minutes,
                "content_html": content_html,
            }
        )

    posts.sort(key=lambda p: (p["date_obj"], p["slug"]), reverse=True)

    all_tags = sorted({tag for p in posts for tag in p["tags"]})
    tag_filter_html = (
        '<button class="tag-pill active" type="button" data-filter="all">All</button>\n'
        + "\n".join(
            f'<button class="tag-pill" type="button" data-filter="{html.escape(t)}">#{html.escape(t)}</button>'
            for t in all_tags
        )
    )

    cards_html = []
    for post in posts:
        tags_attr = html.escape(",".join(post["tags"]))
        tags_html = build_tag_badges(post["tags"], clickable=False)
        cards_html.append(
            f"""<article class="post-card" data-tags="{tags_attr}">
  <div class="post-meta">
    <time datetime="{html.escape(str(post["date_str"]))}">{html.escape(str(post["date_human"]))}</time>
    <span>&middot;</span>
    <span>{post["minutes"]} min read</span>
  </div>
  <h2><a href="posts/{html.escape(str(post["slug"]))}/">{html.escape(str(post["title"]))}</a></h2>
  <p class="post-summary">{html.escape(str(post["summary"]))}</p>
  <div class="post-tags">{tags_html}</div>
</article>"""
        )

    index_body = render_template(
        "index.html",
        tag_filters=tag_filter_html,
        post_cards="\n".join(cards_html),
        post_count=str(len(posts)),
    )
    index_page = render_template(
        "base.html",
        page_title=f"{SITE_TITLE} · {SITE_HANDLE}",
        page_description=html.escape(SITE_DESCRIPTION),
        root_prefix="",
        nav_home_active="active",
        nav_about_active="",
        content=index_body,
    )
    (OUT_DIR / "index.html").write_text(index_page, encoding="utf-8")

    about_body = render_template("about.html")
    about_page = render_template(
        "base.html",
        page_title=f"About · {SITE_TITLE}",
        page_description=html.escape(SITE_DESCRIPTION),
        root_prefix="",
        nav_home_active="",
        nav_about_active="active",
        content=about_body,
    )
    (OUT_DIR / "about.html").write_text(about_page, encoding="utf-8")

    for i, post in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None

        nav_links = []
        if newer:
            nav_links.append(
                f'<a class="pager-link" href="../{html.escape(str(newer["slug"]))}/">'
                f'<span class="pager-label">&larr; Newer</span>'
                f'<span>{html.escape(str(newer["title"]))}</span></a>'
            )
        else:
            nav_links.append("<span></span>")

        if older:
            nav_links.append(
                f'<a class="pager-link right" href="../{html.escape(str(older["slug"]))}/">'
                f'<span class="pager-label">Older &rarr;</span>'
                f'<span>{html.escape(str(older["title"]))}</span></a>'
            )
        else:
            nav_links.append("<span></span>")

        post_body = render_template(
            "post.html",
            post_title=html.escape(str(post["title"])),
            post_date=html.escape(str(post["date_human"])),
            post_date_iso=html.escape(str(post["date_str"])),
            reading_time=str(post["minutes"]),
            post_tags=build_tag_badges(post["tags"], clickable=False),
            post_content=str(post["content_html"]),
            post_pager="\n".join(nav_links),
        )
        full_post = render_template(
            "base.html",
            page_title=f"{html.escape(str(post['title']))} · {SITE_TITLE}",
            page_description=html.escape(str(post["summary"] or SITE_DESCRIPTION)),
            root_prefix="../../",
            nav_home_active="active",
            nav_about_active="",
            content=post_body,
        )
        post_dir = OUT_DIR / "posts" / str(post["slug"])
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.html").write_text(full_post, encoding="utf-8")

    (OUT_DIR / "feed.xml").write_text(build_rss(posts), encoding="utf-8")
    print(f"Built {len(posts)} post(s) into {OUT_DIR}")


if __name__ == "__main__":
    main()
