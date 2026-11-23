---
title: Taming Hyprland's Lua Keybinds: Brightness, Multi-Monitor Swaps & a Stuck Error Bar
date: 2026-11-19
summary: What happened when my external keyboard lacked brightness keys—permissions errors, Lua syntax traps, a stubborn red banner, and dynamic monitor flipping.
tags: [hyprland, shortcuts, lua, arch-linux]
---

My laptop's built-in brightness keys worked fine out of the box, right up until I plugged in an external keyboard that didn't have `XF86MonBrightnessUp` or `Down`.

Picking a shortcut took a couple of tries—`SUPER + =` and `-` were already taken by zoom, so **`SUPER + ALT + Up / Down`** won. Getting Hyprland to actually *accept* it, though, turned into a comedy of errors:

1. **Wrong file & root permissions:** Appending classic `bindel = SUPER ALT, Up, exec, brightnessctl set 5%+` lines to `~/.config/hypr/hyprland.conf` failed with `Permission denied` until I fixed ownership (`sudo chown -R $USER:$USER ~/.config/hypr`)—and even after `hyprctl reload`, nothing happened.
2. **Finding the real config:** Grepping `~/.config/` for `XF86MonBrightnessUp` exposed why: *illogical-impulse* on Hyprland `0.57.2` ignores `hyprland.conf` and loads Lua bindings from **`~/.config/hypr/hyprland/keybinds.lua`**.
3. **The `+` separator trap:** Appending `hl.bind("SUPER ALT, Up", ...)` lit up a bright red **"your config has errors"** bar across the top of my screen. Checking `tail -n 10 keybinds.lua` showed that the Lua helper expects `+` between every key:

```lua
hl.bind("SUPER + ALT + Up", hl.dsp.exec_cmd(qsIpcCall .. " brightness increment || brightnessctl s 5%+"), { flags = "el" })
hl.bind("SUPER + ALT + Down", hl.dsp.exec_cmd(qsIpcCall .. " brightness decrement || brightnessctl s 5%-"), { flags = "el" })
```

Calling `qsIpcCall` first keeps Quickshell's brightness OSD popup working, with `brightnessctl` as a fallback. Funny enough, even after `hyprctl configerrors` came back completely clean and the shortcut worked, that red error banner refused to budge (`hyprctl dismissnotify -1` and `reload config-only` couldn't clear the stale overlay)—and since I refused to close my open apps just to log out, I lived with the banner until my next reboot!

A couple of days later, multi-monitor bindings got the same Lua treatment. I had already put `focusmonitor` on `SUPER + ALT + Left/Right` (learning that `require()` in `custom/keybinds.lua` needs a re-login the first time). When I also wanted a shortcut to flip my external monitor (`HDMI-A-2`) between the left and right side of my laptop on the fly, `hyprctl keyword monitor` failed with `unknown request` in Lua mode—so we wired `SUPER + SHIFT + ALT + Left/Right` straight into Hyprland's native Lua `hl.monitor({ output = "HDMI-A-2", position = "auto-left" })` API instead.

Along the way I also discovered how many shortcuts were *already* built in: `SUPER + Arrows` for window focus, `SUPER + SHIFT + [1-9]` to send windows across workspaces, and `SUPER + /` whenever I need the interactive cheatsheet.
