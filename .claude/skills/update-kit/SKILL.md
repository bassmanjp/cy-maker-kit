---
name: update-kit
description: Update the Cy Maker Kit from GitHub and merge its universal rules, project packs, templates, skills and helpers without losing local lessons. USE WHEN the person types /update-kit or asks to update the kit.
---
# Update the kit

1. The clone is the folder named in `~/.claude/maker-kit/KIT_PATH`
   (usually `~/Projects/cy-maker-kit`). If gone, clone the public repo named
   in `~/.claude/maker-kit/KIT_REPO` into their Projects folder and update
   `KIT_PATH`. Read the repo value; do not substitute a different account.
2. Check the clone's `git status`. If it has local edits, stop the update
   and explain; never discard or stash them automatically.
   Otherwise `git -C <kit path> pull --ff-only`. Explain new commits from
   `git log --oneline ORIG_HEAD..HEAD` in plain words.
3. Compare before reinstalling. Skills go to `~/.claude/skills/`, agents
   to `~/.claude/agents/`; `cy/ knowledge/ packs/ templates/ tools/` and
   `KIT_REPO` go to `~/.claude/maker-kit/`. Update kit-owned files only.
   Preserve local edits and lessons by merging them before copying; keep
   knowledge additions under "Local additions". Skip unrelated same-name
   skills or agents and explain. Never replace whole shared folders.
4. Merge the clone's `cy/USER-CLAUDE.md` into **`~/.claude/CLAUDE.md`**:
   replace only the text between the `cy-maker-kit:start` and
   `cy-maker-kit:end` markers (if there are no markers yet, add them around
   the kit's text the first time).
   Create it only if missing. Keep every existing rule and the person's
   "Our own rules"; show changes and resolve conflicts with them.
   The kit-root `CLAUDE.md` is just a setup pointer, never the installed rules.
5. Existing projects keep their own `CLAUDE.md`. In a hardware project,
   compare it with `packs/hardware/CLAUDE.md` and merge relevant updates,
   preserving project details. Never add hardware rules to other projects.
   For an older install, check for kit hardware rules in `maker/CLAUDE.md` or `Projects/CLAUDE.md`;
   move those rules into the hardware projects that need them, merge the
   universal parts into `~/.claude/CLAUDE.md`, and keep all personal rules.
   Leave a setup pointer in the old file only after every rule is accounted for.
6. Tell them in three lines what is new and what, if anything, needs their hands.
