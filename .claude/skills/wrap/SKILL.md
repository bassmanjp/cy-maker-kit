---
name: wrap
description: End a work session in any project - run its checks, update notes and decisions, commit and push, then say where things stand. USE WHEN the person says wrap up or done for today.
---
# Wrap up

1. Read the project's `CLAUDE.md` and use `test` to run the relevant
   checks for its stack. Use `check` if a feature is ending. Say which
   real-use checks passed and which are still waiting.
2. Update `NOTES.md`: what works, what is next, and what is unverified,
   in five lines or fewer. Include what is wired only in a hardware project.
3. Update `PITFALLS.md` with surprises (symptom, cause, fix) and
   `DECISIONS.md` with choices (what, why, alternatives).
4. A correction to how you work goes in "Our own rules" in
   `~/.claude/CLAUDE.md`, preserving existing rules. Other lessons shared
   across projects can go in the right `~/.claude/maker-kit/knowledge/` file.
5. Check `git status` and the diff for secrets and unrelated changes.
   Commit the working changes **and updated notes** with a plain message,
   then `git push` and confirm it succeeded. Check that the local commit
   matches the remote branch. Unpushed work is not backed up on GitHub.
   If work is incomplete, say so and record the missing check; never call it done.
6. Tell the person in three lines: what works now, what is next, anything
   they need to buy or check before next time.
