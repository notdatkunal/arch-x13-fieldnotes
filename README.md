# Arch Linux + Hyprland on ThinkPad X13 Gen 1

Documentation and capability guide for running **Arch Linux** with **Hyprland** (`end-4/dots-hyprland` / *illogical-impulse* + `uwsm`) on a **Lenovo ThinkPad X13 Gen 1** (Intel Core i5-10310U, Intel UHD Graphics, 16 GB RAM).

- **Live Site (GitHub Pages):** https://notdatkunal.github.io/arch-x13-fieldnotes/

## Contents

- [Why Arch + Hyprland (*illogical-impulse*)](docs/why-arch-hyprland.md) — Why this combination works well, how Hyprland compares to X11/Sway/GNOME/KDE, and maintenance trade-offs.
- [Hardware Specs & Development Capabilities](docs/hardware-and-dev-capabilities.md) — Machine overview, software development sweet spots, and practical resource limits.
- [Content Creation, Live Streaming & Light Video Editing](docs/content-creation-and-streaming.md) — Wayland capture stack, Intel VA-API / Quick Sync hardware encoding, OBS Studio setup tips, and 1080p editing workflows.

## System Snapshot (Sanitized)

| Component | Specification |
| --- | --- |
| **Laptop** | Lenovo ThinkPad X13 Gen 1 |
| **CPU** | Intel Core i5-10310U (4 cores / 8 threads, up to 4.4 GHz boost) |
| **GPU** | Intel UHD Graphics (CometLake-U GT2, integrated) |
| **Memory** | ~16 GB RAM (`15 GiB` usable) + `4 GiB` `zram` swap |
| **Storage** | 476.9 GiB NVMe SSD |
| **Display** | 1920×1080 internal panel (`eDP-1`) |
| **OS & Kernel** | Arch Linux (`7.3.5-arch1-1`) |
| **Compositor & Session** | Hyprland `0.57.2` managed via `uwsm` (`0.27.2`) |
| **Desktop Shell / Dotfiles** | `end-4/dots-hyprland` (*illogical-impulse*, Quickshell-based) |

## TL;DR Verdict

| Workload | Rating | Notes |
| --- | --- | --- |
| **Web, Backend & CLI Development** | Great | Fast NVMe, 15 GiB RAM, Docker, and lightweight tiling overhead (~3.3 GiB idle RAM). |
| **AI-Assisted / Cloud Coding** | Great | Thin-and-light portability paired with lightweight terminals/editors and cloud agents. |
| **Coding & Tutorial Live Streaming** | Good | Works well at **1080p30** or **720p60** in OBS using **VA-API H.264** hardware encoding on AC power. |
| **Light 1080p Video Editing** | Good | Smooth for cuts, voiceovers, and screen recordings (use proxy clips in Kdenlive/Shotcut for complex timelines). |
| **Audio / Podcasts / Thumbnails** | Great | Native PipeWire + WirePlumber routing; GIMP/Inkscape/Audacity run effortlessly. |
| **3D Gaming / Heavy GPU Rendering** | Limited | Fine for 2D/indie/older titles (`vulkan-intel`), not suited for AAA 3D games or heavy Blender rendering. |
| **Local LLMs / ML Training** | Not Ideal | No dedicated GPU/VRAM; only tiny CPU-quantized models are practical locally. |
