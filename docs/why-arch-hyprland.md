# Why Arch Linux + Hyprland (*illogical-impulse*)

The **Arch Linux + Hyprland** combination has become popular because Arch's rolling-release model aligns closely with Hyprland's fast-paced development, while Hyprland balances tiling efficiency with modern Wayland visuals.

---

## 1. Why Arch + Hyprland Together?

* **Rolling, Bleeding-Edge Updates:** Hyprland evolves rapidly—new features, Wayland protocol improvements, and GPU driver updates land frequently. Arch ships the latest kernel, `mesa`, `intel-media-driver`, and Hyprland packages quickly without waiting on fixed distro release cycles or manual source builds.
* **AUR Ecosystem:** Hyprland setups rely on many modular companion utilities (status bars, widget shells, wallpaper daemons, launchers, screen capture helpers). Nearly all of them are available directly in the official Arch repos or the AUR.
* **Minimal Base:** Arch does not ship a heavy desktop environment by default, so there are no background GNOME/KDE session services competing with your window manager.

---

## 2. Why This Specific Setup (`end-4/dots-hyprland` + `uwsm`)?

This setup runs **Hyprland (`0.57.2`)** launched via **`uwsm`** (Universal Wayland Session Manager) with the **`end-4/dots-hyprland`** (*illogical-impulse*) configuration:

* **Quickshell-Powered Desktop UX:** Rather than piecing together a basic bar manually, *illogical-impulse* uses Quickshell (`illogical-impulse-quickshell-git`) to provide integrated widgets, media/system controls, notifications, and visual polish out of the box.
* **`uwsm` Systemd Integration:** Launching Hyprland under `uwsm` (`hyprland-uwsm`) cleanly manages environment variables, XDG portals, and user systemd units—preventing common Wayland issues with portals, screensharing, and app launches.
* **Low Idle Footprint:** Even with widgets and animations enabled, baseline idle memory usage sits around **~3.3 GiB** out of `15 GiB`, leaving generous headroom for development tools.

---

## 3. How Hyprland Compares to Other Setups

| Setup | Key Difference vs. Hyprland |
| --- | --- |
| **X11 Tiling WMs** (`i3`, `bspwm`, `dwm`) | Hyprland runs natively on Wayland (no screen tearing, proper per-monitor fractional scaling and mixed refresh rates) and builds blur, animations, and rounded corners into the compositor without needing `picom`. |
| **Sway** (Wayland) | Sway aims to be a minimal, static i3 replacement on Wayland. Hyprland focuses on dynamic tiling, richer animations, plugins, and visual customization. |
| **Full DEs** (GNOME, KDE Plasma) | Hyprland uses less memory/CPU and prioritizes keyboard-driven window management via plain text config files (`hyprland.conf`). |

---

## 4. Trade-offs & Maintenance Tips

* **Rapid Upstream Changes:** Because both Arch and Hyprland move fast, major Hyprland updates occasionally deprecate config keys or adjust behavior.
* **Keep Dotfiles Synced:** Before large `pacman`/`yay` system upgrades, check upstream changes in `end-4/dots-hyprland` and pull/merge updates so your Quickshell widgets and Hyprland bindings stay compatible.
* **DIY Responsibility:** You trade "never think about it" stability for full control over your desktop stack.
