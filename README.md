# Kunal's Personal Blog (`notdatkunal.github.io`)

Personal blog hosted at **https://notdatkunal.github.io/**. Posts are written in plain **Markdown** under [`posts/`](posts/) and automatically compiled to static HTML and deployed to GitHub Pages on every push to `main`.

## Writing & Publishing a New Post

1. Create a new `.md` file in `posts/`, e.g. `posts/2026-12-01-my-new-post.md`:

```markdown
---
title: My New Post Title
date: 2026-12-01
summary: A short one-line summary for the homepage feed.
tags: [linux, dev]
---

Write normal Markdown here...
```

2. (Optional) Preview locally:

```bash
python3 scripts/build.py
python3 -m http.server -d _site 8000
```

3. Commit and push to `main`:

```bash
git add posts/
git commit -m "post: add my new post"
git push
```

GitHub Actions (`.github/workflows/deploy.yml`) compiles `posts/*.md` into `_site/` and publishes to GitHub Pages automatically.
