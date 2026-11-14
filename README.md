# Cy Maker Kit

A starter kit that helps Claude work with you on every kind of project:
apps, scripts, 3D-print designs, home automation, writing and hardware.
Plan small, check the real result, save to GitHub and write down lessons.
ESP32 is the first pack; its wiring and safety rules apply to hardware projects.

## Set up (about 45 minutes, no terminal, no API keys)

1. Make a folder called `Projects` in your home folder (Finder, ⌘⇧H, New Folder).
2. In the Claude desktop app, open the **Code** tab (not Chat, not Cowork) and
   start a local session on the `Projects` folder. Set the mode next to the
   message box to **Auto** (or Accept edits if Auto isn't there).
3. Paste:
   > Set me up with the Cy Maker Kit: clone
   > https://github.com/bassmanjp/cy-maker-kit into this folder (if git isn't
   > installed, set up Apple's developer tools first), then open
   > cy-maker-kit/START-HERE.md and walk me through it one step at a time.

Claude walks you through seven steps, making your free GitHub account on
the way, and stops only for what needs your hands: an Apple install pop-up,
the GitHub signup and login in your browser, and telling it what you want
to build first.

## Why the Code tab and not Cowork

Cowork works inside a sealed sandbox. The Code tab works right on your
computer, with your files, your tools and anything you plug in (a board, a
printer), and it saves your projects to GitHub. Same app, nothing extra to pay. Cowork
is still great for research and parts lists.

## What's inside

| Folder | What |
|--------|------|
| `START-HERE.md` | the setup wizard Claude follows |
| `CLAUDE.md` | a setup pointer while this kit folder is open |
| `cy/USER-CLAUDE.md` | universal rules merged into `~/.claude/CLAUDE.md`, loaded in every project |
| `cy/ETHOS.md`, `cy/MODELS.md` | how we work and who does what; read by the main session |
| `packs/hardware/` | wiring, safety, build and self-test rules copied into hardware projects |
| `.claude/skills/` | `/architect`, `/plan-project`, `/new-project`, `/flash`, `/test`, `/check`, `/hw-debug`, `/wiring-check`, `/be-ambitious`, `/wrap`, `/guide`, `/update-kit` |
| `.claude/agents/` | helpers: `maker-engineer`, `maker-checker`, `maker-researcher` |
| `knowledge/` | the shared method, Claude pitfalls, plus hardware reference files |
| `templates/basic/` | a starting folder for apps, scripts, designs, automation and writing |
| `templates/esp32-starter/` | PlatformIO project with unit tests, self-test, notes files |
| `tools/` | `doctor.py` (is this computer ready?), `serial_check.py` (did the board pass?) |
