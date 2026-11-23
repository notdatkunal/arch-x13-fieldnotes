---
title: Hunting for a 5G Modem Inside My ThinkPad X13 (and Hitting Lenovo's BIOS Whitelist)
date: 2026-11-17
summary: How checking for a 4G/5G card uncovered Lenovo's strict WWAN BIOS whitelist—and turned into a full ThinkPad hardware upgrade roadmap.
tags: [thinkpad, hardware, arch-linux]
---

Halfway through setting up Arch, I noticed the SIM tray slot on my ThinkPad and wondered: *wait, does this laptop actually have a cellular modem inside?*

I asked `agy` to check. Scanning `lspci`, USB buses, and `/sys/class/net` turned up the Silicon Motion NVMe drive, Intel CNVi Wi-Fi, Gigabit Ethernet, and Thunderbolt 3—but zero `wwan` devices. Even checking the M.2 slots showed the WWAN slot was completely empty.

Naturally, my next thought was to grab a 5G M.2 card off Amazon and drop it in. First I asked `agy` for my model number—which hilariously replied *"I am Gemini 4 Hydrogen"* before I clarified *"model number of this device"* (`20T3S24C0C`, a **Lenovo ThinkPad X13 Gen 1**).

That's when I hit the classic ThinkPad wall: **Lenovo's UEFI BIOS WWAN whitelist**.

* Plugging in a generic or 5G M.2 modem (like a Fibocom FM350-GL) triggers an *"Unauthorized network card is plugged in"* error and refuses to boot.
* The X13 Gen 1 only accepts specific Lenovo FRU-whitelisted **4G LTE** cards (**Fibocom L860-GL** or **L850-GL**)—and only if the laptop shipped as *"WWAN Upgradable"* with antenna leads pre-routed behind the screen.

That dead end turned into a much better question: *what CAN I actually upgrade on this laptop?* While RAM and Wi-Fi are soldered, almost everything else is fair game:

* **Storage:** Swapping the main single-sided `M.2 2280` NVMe up to 2 TB—plus using that empty WWAN slot for a secondary `B+M` key **`M.2 2242` NVMe SSD**.
* **Screen & Input:** Upgrading to a **400-nit low-power 1080p IPS** panel, a backlit ThinkPad keyboard, and fresh low-profile TrackPoint caps.
* **Thermals & Battery:** Repasting with a **`PTM7950`** phase-change thermal pad, swapping in a fresh `L19M3P72` OEM battery (mine is down to ~75% health after 799 cycles), and adding a Thunderbolt 3 dock for desk setups.

No internal 5G—phone tethering wins there—but knowing the exact upgrade ceiling made me appreciate this little ThinkPad way more.
