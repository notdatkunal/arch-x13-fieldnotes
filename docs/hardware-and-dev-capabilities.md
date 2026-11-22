# Hardware Specs & Development Capabilities

## Machine Overview

* **Laptop:** Lenovo ThinkPad X13 Gen 1
* **Processor:** Intel Core i5-10310U (4 cores, 8 threads, up to 4.4 GHz boost, Comet Lake-U)
* **Graphics:** Intel UHD Graphics (CometLake-U GT2, integrated) with `mesa`, `vulkan-intel`, and `intel-media-driver`
* **Memory:** `15 GiB` usable RAM + `4 GiB` `zram` compressed swap
* **Storage:** `476.9 GiB` NVMe SSD
* **Display:** `1920×1080` internal panel (`eDP-1`)
* **Battery Health Note:** Design capacity `48.02 Wh` (with ~75% remaining capacity after ~799 charge cycles—solid for portable sessions, though best plugged in for sustained heavy workloads)

---

## What It Excels At

### 1. Software, Web & Backend Development
* **Toolchains & Runtimes:** Handles Python (`uv`, `ruff`, `basedpyright`), Node.js/TypeScript (`npm`, `tsc`), Rust (`rust-analyzer`), C/C++ (`gcc`, `clang`), and Java comfortably.
* **Containers & Services:** `15 GiB` RAM + `4 GiB` `zram` + NVMe SSD is a sweet spot for running Docker / Docker Compose stacks alongside an editor (`neovim`, VS Code, or PyCharm/IDEA) and browser tabs.
* **Fast Feedback Loops:** `1080p` screen real estate paired with Hyprland's tiling splits makes side-by-side terminal, editor, and browser workflows fast without external monitors (and dual DP/HDMI outputs are available via USB-C/HDMI when docked).

### 2. Cloud-Backed & Agentic Coding Workflows
* Lightweight terminal/editor setups (`ghostty`, `kitty`, `neovim`, VS Code) combined with cloud-hosted AI coding assistants perform smoothly without needing discrete GPU hardware.

### 3. General Linux Engineering & Homelab Control
* Well suited for SSH/remote server management, API load testing (`wrk`), security scanning (`gitleaks`), Git workflows (`lazygit`, `gh`), and lightweight local virtualization.

---

## Practical Limits

1. **Local LLMs / ML Training:** Integrated Intel UHD Graphics has no dedicated VRAM or CUDA support. Only very small CPU-quantized models are viable locally.
2. **Heavy Simultaneous VMs / Huge Monorepo Builds:** A 4-core/8-thread ultrabook CPU handles normal projects smoothly, but running multiple heavy VMs or large C++/Rust builds alongside heavyweight IDEs and dozens of browser tabs will saturate CPU and RAM.
3. **Demanding 3D Gaming & GPU Compute:** Good for 2D, indie, or older games via `vulkan-intel`, not meant for modern AAA 3D titles or GPU-heavy Blender rendering.
