---
title: Stopping Idle Suspends, Testing Streaming Limits & Accidentally Claiming My Root GitHub URL
date: 2026-11-22
summary: Fixing hypridle so builds don't sleep, discovering Intel VA-API streaming on my ThinkPad, and turning my agy sessions into this blog.
tags: [arch-linux, hyprland, streaming, thinkpad, github-pages]
---

Nothing kills momentum faster than walking away for coffee while a build or `agy` task is running, only to come back to a suspended laptop. Checking `hypridle.conf` showed why: *illogical-impulse* defaulted to locking at 5 minutes, turning the screen off at 10, and suspending the whole machine at **15 minutes (`900s`)**. Bumping both lock and DPMS screen-off to **20 minutes (`1200s`)**—and deleting the auto-suspend listener altogether—solved that for good.

With the setup dialed in, I asked `agy` two big-picture questions: *why is the Arch + Hyprland combo so popular in the first place, and what is my hardware actually capable of?*

For software and cloud-agent workflows, my **ThinkPad X13 Gen 1** (`i5-10310U` 4c/8t, `15 GiB` usable RAM + `4 GiB` `zram`, ~`3.3 GiB` idle RAM) is right in its element—excluding local LLMs or AAA 3D games since Intel UHD Graphics has no dedicated VRAM. The real surprise came when I asked about **light video editing and live streaming**:

* My Wayland capture stack (`xdg-desktop-portal-hyprland`, `pipewire`, `wireplumber`, `wf-recorder`, `slurp`, `swappy`) and webcams (`/dev/video0`) were *already* wired up.
* Thanks to `intel-media-driver`, `ffmpeg` already exposed **Intel Quick Sync / VA-API** hardware encoders (`h264_vaapi`, `hevc_vaapi`, `h264_qsv`).
* That means **1080p light editing** in Kdenlive/Shotcut (using proxy clips for heavier timelines) and **1080p30 / 720p60 coding streams in OBS** work smoothly—as long as I pick `FFmpeg VAAPI H.264` instead of software `x264`, stay plugged into AC power (so `intel_pstate` doesn't throttle on `powersave`), and capture a full monitor or dedicated workspace in Hyprland.

When I asked `agy` to document all of this on GitHub—after refreshing an expired `gh` token and configuring GitHub's noreply email—what started as a static repo evolved into this personal blog: plain Markdown files compiled to HTML automatically by Python and GitHub Actions.

Best surprise at the very end? Naming the repository **`notdatkunal.github.io`** made GitHub treat it as my User Pages site, serving it straight from **`https://notdatkunal.github.io/`** instead of a `/repo-name` subpath—a clean home for every rabbit hole I explore next.
