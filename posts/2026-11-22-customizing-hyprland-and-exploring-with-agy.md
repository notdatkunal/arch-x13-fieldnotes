---
title: Tweaking Hyprland & Exploring My Setup with agy CLI
date: 2026-11-22
summary: Notes from my agy CLI sessions—customizing Lua brightness shortcuts, fixing hypridle timeouts, debugging ThinkPad quirks, and mapping hardware upgrades.
tags: [agy-cli, hyprland, shortcuts, thinkpad, arch-linux]
---

Most of my recent tinkering on Arch happened inside **`agy` (Antigravity CLI)**—using it to debug config syntax, explore built-in Hyprland shortcuts, stop my laptop from sleeping mid-task, and plan out ThinkPad hardware upgrades.

Here's a compiled log of what I customized, why I changed it, and what I found along the way.

---

## 1. The Brightness Shortcut Rabbit Hole (`SUPER + ALT + Up/Down`)

### Why I Added It
ThinkPads already have `XF86MonBrightnessUp` and `XF86MonBrightnessDown` on the function row, **but** when I'm typing fast with my hands centered on the keyboard (or working in low light without hunting for `Fn` keys), having a `SUPER + ALT + Up / Down` shortcut feels much faster.

### What Broke First (and Why)
I hit three classic gotchas before it worked cleanly:

1. **Wrong Config File Format:** I initially tried appending classic `.conf`-style lines (`bindel = SUPER ALT, Up, exec, brightnessctl set 5%+`) to `hyprland.conf`. That didn't play nicely with `end-4/dots-hyprland` on Hyprland `0.57.2`, which defines keybinds in **Lua** (`~/.config/hypr/hyprland/keybinds.lua`) using `hl.bind(...)`.
2. **File Ownership:** At one point `~/.config/hypr` had permission friction until I normalized ownership (`sudo chown -R $USER:$USER ~/.config/hypr`).
3. **Lua Key Syntax (`hyprctl configerrors`):** When I moved into `keybinds.lua`, writing `"SUPER ALT, Up"` threw config errors on `hyprctl reload`. Checking the surrounding lines in `keybinds.lua` showed why: *illogical-impulse*'s Lua helper joins modifiers and keys with **`+`** instead of commas!

### What Worked
The final custom bindings appended to `~/.config/hypr/hyprland/keybinds.lua` (around line 360):

```lua
hl.bind("SUPER + ALT + Up", hl.dsp.exec_cmd(qsIpcCall .. " brightness increment || brightnessctl s 5%+"), { flags = "el" })
hl.bind("SUPER + ALT + Down", hl.dsp.exec_cmd(qsIpcCall .. " brightness decrement || brightnessctl s 5%-"), { flags = "el" })
```

* **Why `qsIpcCall ... || brightnessctl`?** It calls Quickshell's IPC brightness handler first (so the sleek on-screen brightness OSD pops up), and falls back to `brightnessctl` if Quickshell isn't running.
* **Why `flags = "el"`?** `e` repeats while held down, and `l` lets it work even on the lock screen (in newer Lua helper style in `keybinds.lua`, you'll also see `{ locked = true, repeating = true }`).
* **Verification commands that saved me:**
  * `hyprctl configerrors` — immediately catches bad keybind syntax.
  * `hyprctl binds | grep -i brightness` — confirms the bind actually loaded.
  * `hyprctl reload` — reloads on the fly without logging out.

---

## 2. Built-in Shortcuts I Explored & Kept Using

Digging through `keybinds.lua` reminded me how many useful shortcuts *illogical-impulse* already ships with—these are the ones I keep reaching for:

| Shortcut | Action | Why It's Useful |
| --- | --- | --- |
| `SUPER + Slash` | Toggle Quickshell cheatsheet | Quick reminder whenever I forget a bind |
| `SUPER + SHIFT + S` | Region screenshot (`hyprshot`) | Instant snip to clipboard |
| `SUPER + SHIFT + X` | Region OCR (`tesseract`) | Grabs text straight out of images/videos into clipboard |
| `SUPER + SHIFT + C` | Color picker (`hyprpicker -a`) | Copies `#RRGGBB` hex right to clipboard |
| `SUPER + SHIFT + R` | Record screen region | Quick clips without opening a heavy studio app |
| `SUPER + V` | Clipboard history | Essential when hopping between terminal and browser |
| `CTRL + SUPER + R` | Restart Quickshell widgets | Handy if the shell ever needs a quick refresh |

I also explored CLI ways to clear stuck notifications or refresh the shell when experimenting (`hyprctl dismissnotify -1`, `hyprctl reload config-only`, and `pkill qs && qs &`).

---

## 3. Stopping Mid-Work Suspends (`hypridle.conf`)

By default, `dots/.config/hypr/hypridle.conf` locked the screen after 5 minutes (`300s`), turned off the display after 10 minutes (`600s`), and **suspended the laptop after 15 minutes (`900s`)**.

That got annoying fast whenever I left Docker builds, updates, or long `agy` agent runs going in the background. I tweaked `hypridle.conf` to:

* Bump `loginctl lock-session` to **20 minutes** (`1200s`)
* Bump display DPMS off to **20 minutes** (`1200s`)
* **Remove the 15-minute `suspend` listener** completely so background tasks finish reliably while plugged in

---

## 4. Fixing ThinkPad Wi-Fi & Bluetooth Quirks

Early on, I also spent time stabilizing ThinkPad wireless hardware on Arch:

* **Wi-Fi:** Tested low-level `iwlwifi` / `rfkill` / `wpa_supplicant` + `systemd-networkd` vs `NetworkManager`, and settled on `NetworkManager` (`nmcli` / `nmtui`) for reliable day-to-day switching.
* **Bluetooth HID:** Loaded `uhid` (`sudo modprobe uhid`) alongside enabling `bluetooth.service` so Bluetooth peripherals pair and behave properly.

---

## 5. ThinkPad X13 Gen 1 Upgrade Rabbit Hole (via `agy`)

In one `agy` session, I mapped out potential upgrades for the ThinkPad X13 Gen 1 to give it even more headroom down the road:

* **Storage:** Single-sided `M.2 2280` NVMe upgrade (e.g. 2 TB) + exploring a `B+M` key `M.2 2242` NVMe in the WWAN slot
* **Display & Input:** 400-nit low-power `1080p` 30-pin eDP panel, backlit ThinkPad keyboard, and low-profile TrackPoint caps
* **Thermals & Power:** `PTM7950` phase-change thermal pad, OEM battery replacement (`L19M3P72` / `L19C3P72` since mine is ~75% health after 799 cycles), and a Thunderbolt 3 dock for desk work
