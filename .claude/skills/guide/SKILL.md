---
name: guide
description: Explain how this setup works for any project - sessions, slash commands, helpers, models, GitHub and the daily routine - in friendly plain words. USE WHEN the person types /guide, asks "how does this work", "what can you do", "what commands are there", or seems lost.
---
# Guide

Ask which topic they want, or offer the list. Explain one at a time, short,
with an example from their own project when there is one.

1. **Chat, Cowork, Code.** Chat talks. Cowork does office-style tasks in a
   sandbox. Code works on a project folder on your computer and runs its
   tools. This kit uses Code for apps, scripts, designs, automation and writing.
2. **Sessions and folders.** One session = one task in one project folder.
   The Projects folder holds every kind of project. New task, new session;
   notes carry what matters forward. Shared rules in `~/.claude/CLAUDE.md`
   apply everywhere; each project's `CLAUDE.md` adds its own checks.
3. **Slash commands** (type `/` to see them):
   - `/architect`: read the project, say where it stands and what to do next.
   - `/plan-project`: goal, tools, small steps and checks, reviewed.
   - `/new-project`: ask the kind of project and choose its template.
   - `/test`: find and run this project's tests or propose a useful first check.
   - `/check`: a fresh-eyes review before calling a feature done.
   - `/be-ambitious`: think about what the goal is really for.
   - `/wrap`: notes, commit, push, what's next.
   - `/guide`: this. `/update-kit`: get the newest kit.
4. **A normal session.** Open the project in Code, `/architect`, say what
   you want, plan, build in small steps, check in real use, `/wrap`.
5. **Helpers and models.** The main session thinks and talks to you.
   `maker-engineer` builds, `maker-checker` reviews, `maker-researcher`
   reads. You do not manage them. The main session follows
   `~/.claude/maker-kit/cy/MODELS.md`.
6. **Who decides.** Claude decides the technical how. You decide purpose,
   money, safety, installs, sending things to others and deleting unsaved work.
7. **GitHub.** Your projects' safe copy and history, private to you. Claude
   pushes every working step; `/wrap` checks it. `/update-kit` gets kit
   improvements. Never put passwords or private keys in a commit.
8. **Auto mode.** Keep sessions on Auto (mode picker next to the message
   box): Claude works without asking at every step and stops on its own for
   anything risky. If it asks about deleting or installing, read the line.
9. **Usage.** Your plan has an allowance. Long sessions and high effort
   use more: new task, new session.
10. **Lessons.** Status in `NOTES.md`, surprises in `PITFALLS.md`,
    choices in `DECISIONS.md`. Corrections to Claude's habits go in
    "Our own rules" in `~/.claude/CLAUDE.md`.

## When the project is hardware

The hardware pack adds wiring and power rules to the project's `CLAUDE.md`.
Use `/wiring-check` before connecting a part, `/flash` to upload and read
the board's self-test, and `/hw-debug` for board trouble. Pins are 3.3 V
on ESP32; motors and LED strips need separate power with a shared ground.
Never wire wall power; unplug USB before rewiring.
