---
name: new-project
description: Start any kind of project from the right template, fill in its goal and checks, and save the first working step to a private GitHub repo. USE WHEN the person wants to build something new or start a project.
---
# New project

1. Ask what they want to make and **what kind of project it is**: hardware
   with a board, an app, a script, a 3D-print design, home automation,
   writing, or something else. Ask for the exact board only for hardware.
2. Choose the template under `~/.claude/maker-kit/templates/`:
   - **ESP32/Arduino board:** copy `esp32-starter/`. Its `CLAUDE.md`
     is a copy of `packs/hardware/CLAUDE.md`; keep it in the new project.
     If `pio --version` fails, follow
     `~/.claude/maker-kit/packs/hardware/SETUP.md` first.
   - **Other electronics** (Raspberry Pi Pico or Pi, sensors, relays,
     batteries, motors, LED strips): copy `basic/` and also put
     `packs/hardware/CLAUDE.md` in it, so the safety rules apply.
   - **Anything else:** copy `basic/` only.
   Use a new folder (lowercase, dashes) next to their other projects in the
   Projects folder, never inside the kit. If the folder exists, stop and ask
   where to put the new project; never overwrite it.
3. Set it up for what they want:
   - **Hardware:** in `platformio.ini`, set `[env:board]` `board =`:
     - ESP32 DevKit (WROOM-32, CP2102/CH340): `esp32dev`.
     - ESP32-S3 DevKitC: `esp32-s3-devkitc-1`.
     - ESP32-C3 DevKitM: `esp32-c3-devkitm-1`.
     - ESP32-C3 SuperMini: `esp32-c3-devkitm-1` plus
       `build_flags = -DARDUINO_USB_CDC_ON_BOOT=1 -DLED_PIN=8`
       (plain LED, not RGB).
     - Native-USB-only boards (C3 SuperMini, XIAO, S3 on its "USB" port):
       add `-DARDUINO_USB_CDC_ON_BOOT=1` before the first flash.
     - Arduino Uno: use the ready `[env:uno]`; read `-e uno` wherever
       the skills say `-e board`.
     - Anything else: look it up with `pio boards <word>` and current
       maker docs; add the right environment, never guess.
     LED and BOOT pins are chosen in `src/main.cpp` and printed at boot;
     override with `-DLED_PIN=` / `-DBUTTON_PIN=` when needed.
   - **Other software:** choose the simplest standard stack that fits.
     Say why in one line (for example, plain HTML for a simple page, Python
     for a small file-processing script). Ask before installs.
   - **Design, writing or another kind:** use the simplest suitable file
     format and tools; do not add a software stack without a reason.
   Fill in the README and the project's `CLAUDE.md`: what it is, its
   tools, and exactly how to test or check it in real use. In hardware,
   add those project details alongside the pack rules.
4. Use `plan-project` for anything bigger than an afternoon; for hardware,
   also use it for work beyond the starter blink.
5. Run `test` and the project's documented build or practical check.
   Hardware: `pio test -e native`, then `pio run -e board` (or the
   chosen environment), then `flash` when the board is connected.
   Other projects: test the smallest useful result in the chosen tools.
   Record what was actually seen working in `NOTES.md`, and any check
   still waiting. Fix failures before calling a step working.
6. In the new folder, `git init`. If commit identity is missing, ask which
   name and email to use. Review `git status` and the diff for secrets
   and generated files; keep them out of git. Stage this project's files
   and make the first commit, including its notes.
7. `gh repo create <name> --private --source . --push`.
   Confirm the push succeeded and the local HEAD matches the remote branch
   (`git rev-parse HEAD`, `git ls-remote origin refs/heads/<branch>`).
   Give the repo link. If `gh` is missing or logged out, follow step 2 of
   `START-HERE.md` in the kit folder named in `~/.claude/maker-kit/KIT_PATH`. If creation or push fails, say the backup is not ready;
   do not claim the project is saved on GitHub.
