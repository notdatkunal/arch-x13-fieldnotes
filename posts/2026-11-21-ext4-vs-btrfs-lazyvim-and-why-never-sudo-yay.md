---
title: Peeking Under My Arch Hood: ext4 vs Btrfs, LazyVim, and Why Never sudo yay
date: 2026-11-21
summary: Auditing my filesystem and UKI bootloader, surviving LazyVim's silent first-boot freeze, and comparing yay, uv, Nix, and Docker.
tags: [arch-linux, btrfs, neovim, yay, nix]
---

Once my day-to-day setup stabilized, I got curious about what `archinstall` had actually configured underneath—and what Arch veterans usually add on top.

Asking `agy` to inspect my disk and boot setup revealed I was running **`ext4`** on `/dev/nvme0n1p2` with **`systemd-boot`** booting a **Unified Kernel Image (UKI)** (`arch-linux.efi`), backed by `zram` compressed swap and `fstrim.timer`.

Could I switch my root filesystem to **Btrfs** right from inside the running OS? Hard no—converting a live mounted root partition is a recipe for data loss (Live USB + backups only). Understanding *why* people love Btrfs on rolling-release Arch made total sense though: Copy-on-Write (`CoW`) lets tools like `Snapper` or `Timeshift` take sub-second snapshots before `pacman -Syu`, so if an update ever goes sideways you roll back from the boot menu in seconds. Auditing my setup also highlighted a few easy safety nets worth adding even on `ext4`: keeping `linux-lts` installed as a backup kernel, automating package cache cleanup (`paccache.timer`), and enabling a basic host firewall (`ufw`).

That same afternoon turned into a tooling speedrun:

* **Bootstrapping LazyVim:** I already had Neovim `v0.12.6`, so we cloned the **LazyVim** starter into `~/.config/nvim`. On first launch I thought it was completely broken—until `agy` explained Lazy.nvim was quietly downloading and compiling all starter plugins in the background. Once synced, `<Space>l` brought up the clean dashboard.
* **`yay` vs `uv` vs `Nix` vs `Docker`:** Wondering if I should use `brew` or `Nix` instead of `pacman`, I learned how each fits on Arch: **`yay`** for native system & AUR apps, **`uv`** (`uv tool install`) for isolated Python CLIs, **`Nix`** if I ever want disposable zero-conflict dev shells (`nix shell`) directly on the host without container friction, and **`Docker`** when isolating full services and networks.
* **Why Never `sudo yay`:** Finally, asking how to update with `yay` (literally just typing `yay`!) taught me why **`sudo yay` is a major security risk**. Because the **AUR (Arch User Repository)** hosts community `PKGBUILD` build recipes rather than pre-compiled binaries, running `yay` as root would execute arbitrary third-party build scripts with full root privileges—which is why `makepkg` flatly refuses to run as root, and `yay` waits until the final `pacman -U` step to ask for `sudo`.
