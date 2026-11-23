---
title: Trimming Duplicate PyCharm Installs and Testing OpenIDEA ("IntelliJ in Rust?")
date: 2026-11-20
summary: Cleaning up two PyCharms on disk, digging into Reddit's debate over OpenIDEA's Rust claims, and wiring up local LSPs on Arch.
tags: [arch-linux, dev-setup, ide, rust, python]
---

While connecting to a PostgreSQL container on Arch—first setting up a tiny `pg()` shell wrapper around `docker compose exec` so I wouldn't need `psql` on the host, then opening PyCharm's Database tool with `Ctrl + Shift + A` (and wondering why it suddenly started downloading JDBC drivers on demand)—I noticed something weird: I had **two separate PyCharms** sitting on my SSD.

One was `pycharm-community-edition` installed system-wide at `/usr/share/pycharm`, and the other was **PyCharm Professional** tucked inside `~/.local/share/JetBrains/`. Once I confirmed that JetBrains unified PyCharm starting in `2025.1`—meaning the Pro install still keeps every free Community feature even without an active subscription—I nuked the duplicate system package (`sudo pacman -Rns pycharm-community-edition`).

That same afternoon I stumbled across **OpenIDEA** on GitHub, pitched as an open-source, lightweight IntelliJ alternative built with Rust, and asked `agy` to check what Reddit actually thought of it. The community breakdown was super clarifying:

* **The Reality Check:** Despite the *"rebuilt in Rust"* hype, the repo is roughly 60% TypeScript running inside a **Tauri v2** OS WebView, and relies on standard **Language Server Protocol (LSP)** binaries rather than JetBrains' twenty-year-old PSI refactoring engine (unlike pure GPU-rendered Rust editors such as Zed).
* **Why People Still Like It:** If your muscle memory loves JetBrains' layout, `Double-Shift` (Search Everywhere), and built-in Database + HTTP Client panels—normally locked behind paid Ultimate tiers—it gives you a snappy polyglot editor without waiting on the JVM.

Instead of replacing JetBrains completely, keeping both made the most sense: JetBrains for heavy framework surgery, and OpenIDEA (`v0.1.49` AppImage) for fast everyday polyglot edits. We extracted its icon to match my PyCharm Pro desktop entry, linked `openidea` into `~/.local/bin`, and wired up LSPs across `~/.local/bin` (`basedpyright-langserver` and `ruff` via `uv`, `typescript-language-server`, `rust-analyzer`, plus `clangd`—leaving `gopls` and `jdtls` one `pacman`/`yay` command away whenever I need Go or Java).
