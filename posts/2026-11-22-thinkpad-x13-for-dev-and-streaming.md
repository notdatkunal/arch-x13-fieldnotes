---
title: What My ThinkPad X13 Is Actually Good For (Dev, Streaming & Light Editing)
date: 2026-11-22
summary: Auditing my Arch + ThinkPad X13 Gen 1 with agy to see where it shines for coding, live streaming, and 1080p video editing—and where it hits a wall.
tags: [thinkpad, dev-setup, streaming, video-editing, agy-cli]
---

After living on my ThinkPad X13 Gen 1 (`i5-10310U`, 4 cores / 8 threads, Intel UHD Graphics, `15 GiB` usable RAM + `4 GiB` `zram`, `476.9 GiB` NVMe) for a bit, I used `agy` to run a realistic audit of what this machine can actually handle—beyond just "it runs Linux."

---

## Software & AI-Assisted Development: The Sweet Spot

For daily software engineering, this setup punches well above its weight:

* **Backend, Web & CLI Dev:** Python (`uv`, `ruff`, `basedpyright`), Node.js/TypeScript (`npm`, `tsc`), C/C++ (`gcc`, `clang`), Rust (`rust-analyzer`), and Docker / Docker Compose all run comfortably with plenty of memory headroom.
* **Lightweight Tiling + Cloud Agents:** Pairing Hyprland + `ghostty` + `neovim` / VS Code with cloud-backed AI coding tools (`agy`, `claude`, `orca`) gives me a fast, portable workflow without carrying a heavy workstation laptop.
* **Where it tops out:** Running multiple heavy VMs at once, huge C++/Rust monorepo compiles alongside PyCharm + 50 browser tabs, or **local LLMs / ML training** (integrated Intel UHD has no dedicated VRAM or CUDA).

---

## Content Creation & Light Video Editing (1080p)

I wasn't sure how well an ultrabook with integrated graphics would handle video work, so I checked the media stack and codecs already on the system:

* **Wayland Capture Ready:** `xdg-desktop-portal-hyprland`, `pipewire`, `wireplumber`, `wf-recorder`, `slurp`, `swappy`, and webcam devices (`/dev/video0`, `/dev/video1`) are all already wired up.
* **Hardware Acceleration via Intel Quick Sync / VA-API:** With `intel-media-driver` installed, `ffmpeg` exposes `h264_vaapi`, `hevc_vaapi`, `h264_qsv`, and `hevc_qsv`.

### Light Editing Verdict
* **Great for:** 1080p coding walkthroughs, screen recordings, voiceovers, trims/cuts (`ffmpeg` / LosslessCut), and simple Kdenlive/Shotcut timelines.
* **Tip:** Turn on **proxy clips** if a timeline starts stacking effects or high-bitrate clips, and keep an eye on the `476.9 GiB` NVMe drive since raw captures grow fast.

---

## Live Streaming (OBS Studio on Hyprland)

Streaming **coding sessions, browser demos, or podcasts** at **1080p30** or **720p60** works well—as long as I respect the thermal budget of a 4-core U-series chip:

1. **Use `FFmpeg VAAPI H.264` in OBS, not software `x264`:** Letting Intel's media engine encode keeps CPU temperatures and fan noise down while an IDE and browser are open.
2. **Always plug into AC power:** On battery, `intel_pstate` sits on `powersave` and throttles early under sustained load.
3. **Capture a Monitor or Dedicated Workspace:** Because Hyprland tiles windows dynamically, capturing a full screen or dedicated stream workspace avoids jarring aspect-ratio jumps when opening terminal splits.
4. **Skip 3D-game + stream combos:** Playing a demanding 3D game *and* live-encoding on the same Intel UHD iGPU will bottleneck quickly.

---

## Starter Packages When I'm Ready to Record/Edit

```bash
sudo pacman -S obs-studio kdenlive libva-utils
yay -S losslesscut-bin
```

Then `vainfo` lets me verify active VA-API profiles anytime.
