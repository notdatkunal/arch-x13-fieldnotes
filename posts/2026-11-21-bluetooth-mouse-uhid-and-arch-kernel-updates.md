---
title: When "Mic" Meant Mouse: Why My Bluetooth Mouse Stopped Moving After pacman -Syu
date: 2026-11-21
summary: A funny typo sent agy down a Bluetooth audio rabbit hole—before "uhid not found" taught me a classic Arch Linux kernel update lesson.
tags: [arch-linux, bluetooth, kernel, troubleshooting]
---

This one started with a hilarious miscommunication. I typed into `agy`: *"this arch linux distro not supporting to bluetooth mic now."*

Naturally, `agy` thought **mic** meant *microphone* and handed me a full masterclass on PipeWire `1.6`, WirePlumber `0.5`, and why Bluetooth headsets get stuck in one-way `A2DP` playback instead of bidirectional `HSP/HFP` voice profiles. Helpful to know—except I had to reply: *"why are we worrying about bluetooth audio, I just meant the mice!"*

Here was the actual mystery: my Bluetooth mouse paired fine and showed **Connected** inside `bluetoothctl`, yet moving it and clicking did absolutely nothing on screen.

With Bluetooth Low Energy (BLE) mice using HID-over-GATT, Linux needs the **`uhid`** (user-space HID) kernel module to create `/dev/input/event*` nodes. So I ran:

```bash
sudo modprobe uhid
```

And Arch immediately shot back: **`uhid not found`**.

That three-word error gave away the whole plot:

* My **running kernel** in RAM was still `7.2.15-arch1-1`.
* Earlier I had run `sudo pacman -Syu`, which upgraded the kernel on disk to **`7.3.5-arch1-1`** (`/lib/modules/7.3.5-arch1-1/kernel/drivers/hid/uhid.ko.zst`) and cleaned out the old `7.2.15` module folder!

Because Arch removes the previous kernel's `/lib/modules/` directory during an upgrade, any kernel module that wasn't *already* loaded into memory before `pacman -Syu` simply cannot be loaded until you reboot into the new kernel. One `sudo reboot` later, `uhid` loaded cleanly and my mouse sprang right back to life—my favorite classic Arch Linux lesson so far.
