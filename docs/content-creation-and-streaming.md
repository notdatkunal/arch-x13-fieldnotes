# Content Creation, Live Streaming & Light Video Editing

For **coding tutorials**, **screen-recorded demos**, **non-gaming live streams**, and **light 1080p video editing**, this setup is very capable when configured to use Intel's hardware media engine rather than pure CPU encoding.

---

## 1. Ready-to-Use Capture & Media Stack

The system already has the core Wayland media plumbing installed:

* **Screen & Window Portals:** `xdg-desktop-portal-hyprland` (`1.5.0-1`) enables clean screen/window sharing on Wayland.
* **Audio/Video Routing:** `pipewire` (`1:1.6.11-2`) and `wireplumber` (`0.5.19-1`) handle low-latency microphone and desktop audio capture.
* **Built-in Capture Tools:** `wf-recorder` (`0.6.0-2`), `grim`, `slurp`, `hyprshot`, `swappy`, `v4l-utils`, and `ffmpeg` are already present (via `illogical-impulse-screencapture`), with webcam devices (`/dev/video0`, `/dev/video1`) detected.
* **Hardware Acceleration:** `intel-media-driver` (`26.3.5-1`) enables Intel Quick Sync / VA-API hardware encoding and decoding in `ffmpeg` (`h264_vaapi`, `hevc_vaapi`, `h264_qsv`, `hevc_qsv`, `vp9_vaapi`).

---

## 2. Light Video Editing (1080p)

### Where It Works Well
* **1080p screen recordings and talking-head videos** (tutorials, walkthroughs, YouTube dev logs).
* Trimming, cutting, voiceover mixing, basic text overlays, and simple transitions.
* Fast lossless slicing/trimming with `ffmpeg` or **LosslessCut** (`losslesscut-bin`).

### Limits & Workarounds
* **4K timelines, heavy color grading, stabilization, or stacked blur effects** will stutter during timeline scrubbing on Comet Lake UHD Graphics.
* **Use Proxy Clips:** In **Kdenlive** or **Shotcut**, enable proxy clip generation so the timeline edits smoothly at lower resolution while final exports render from the full-resolution source files.
* **Mind Disk Space:** Keep an eye on the `476.9 GiB` NVMe drive—uncompressed or high-bitrate screen recordings add up quickly.

---

## 3. Live Streaming (OBS Studio on Hyprland)

### Realistic Target
* **Ideal for:** Coding streams, terminal/browser demos, slides, podcasts, and 2D/lightweight games at **1080p30** or **720p60** (`4500–6000 kbps`).
* **Not suited for:** Playing demanding 3D games while live-encoding on the same integrated GPU.

### Key Configuration Tips for This Laptop

1. **Use Hardware VA-API H.264 in OBS (Avoid Software `x264`):**
   * The i5-10310U is a 4-core/8-thread thin-and-light CPU. Running software `x264` encoding alongside OBS scene compositing, an IDE, and a browser causes high temperatures and thermal throttling.
   * Select **FFmpeg VAAPI H.264** in OBS output settings so the Intel UHD media engine handles encoding.
2. **Always Stream on AC Power:**
   * On battery, `intel_pstate` defaults to the `powersave` governor and tighter power limits. Plugging into AC with unobstructed airflow prevents early throttling during sustained encodes.
3. **Capture a Monitor or Dedicated Workspace in Hyprland:**
   * Because Hyprland tiles and resizes windows dynamically, capturing a specific **Monitor/Display** (or isolating your demo onto a dedicated workspace) avoids awkward aspect-ratio jumps when opening or closing terminal splits.
4. **Skip Heavy Real-Time Webcam Effects:**
   * Software AI background removal/blur plugins consume significant CPU/iGPU headroom during live streams; use physical lighting/framing instead where possible.

---

## 4. Audio, Thumbnails & Quick Clips

* **Voiceovers & Podcasts:** `pipewire` + `wireplumber` plus lightweight editors like **Audacity** or **Tenacity** use minimal CPU.
* **Thumbnails & Annotations:** `swappy` (already installed) handles quick screenshot markup, and **GIMP** / **Inkscape** run smoothly for thumbnails and diagrams.
* **Quick Terminal Clip Recording:** `wf-recorder` + `slurp` already lets you capture a region directly from Hyprland without opening a full studio suite.

---

## 5. Recommended Packages to Add

These are not installed by default yet and can be added as needed:

```bash
# Streaming, video editing, and VA-API diagnostics
sudo pacman -S obs-studio kdenlive libva-utils

# Optional: lossless trimming (AUR) and audio editing
yay -S losslesscut-bin
sudo pacman -S audacity
```

After installing `libva-utils`, verify active hardware encode/decode profiles anytime with:

```bash
vainfo
```
