---
name: check
description: Independent check of finished work in any project - tests, a fresh-eyes maker-checker review, fixes and a real-use check. USE WHEN a step or feature is built, before saying it works or ending a feature.
---
# Check, then ship

**When the reviewer is needed.** A small change under about 30 lines may
skip `maker-checker` if it touches no dependencies, secrets, saved data,
security or safety. In hardware, it must also touch no pins, power or
wiring. The tests and a real-use check still apply. Always use the reviewer
before ending a feature, or for any safety, security or data-loss risk.
Hardware additions such as motors, batteries, relays or new parts need it.

1. Read the project's `CLAUDE.md` and detect its tools from the project
   files. Use `test` to run its tests, then its documented build if it has
   one. Say if tests or a build do not exist; agree a practical check.
2. Launch `maker-checker` with the goal, the planned check, the commit
   range or `git diff`, the project rules, and "tell me what you could not verify".
3. Fix and recheck blocking findings: a missed requirement, failing test,
   regression, safety problem, exposed secret or possible data loss. Fix
   other findings if cheap; otherwise list them as known limits in `NOTES.md`.
4. Two review rounds at most, then ship with known limits. Blocking findings
   still need fixing; the round limit does not make them acceptable.
5. Run the planned check in the real thing: the app, the script, the
   printed part or the finished writing. For hardware, use `flash` and
   check the board. Done only when that check passes; say what remains unverified.
