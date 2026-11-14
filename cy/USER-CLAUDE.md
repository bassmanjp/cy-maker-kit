<!-- cy-maker-kit:start (kit rules; /update-kit replaces only this block) -->
# How we work together

These rules apply to every project: an app, a script, a printed part, home
automation, writing, or hardware. The person is learning; you do the work
and commands, and explain in plain English. They handle anything that
needs their hands. Follow the project's `CLAUDE.md` for its own tools and checks.

How we work: @~/.claude/maker-kit/cy/ETHOS.md
Which model and helper does what: @~/.claude/maker-kit/cy/MODELS.md

## The loop

1. **Say the goal and the check.** What should happen, and how will we see
   it working in the real thing: the app, the board, the printed part, or
   the finished piece of writing?
2. **Take the smallest step.** One useful change at a time.
3. **Keep logic testable.** Separate it from devices, screens and outside
   services. Run the project's tests; use a practical check for a design or
   a piece of writing. The `test` skill finds the right starting point.
4. **Done means seen working.** A successful build alone is not enough.
   Run the check from step 1. Say plainly what you could not check.
5. **Write it down.** Keep where things stand and what is next in `NOTES.md`.
   Surprises and fixes go in `PITFALLS.md` (symptom, cause, fix); choices go
   in `DECISIONS.md` (what, why, what else was considered).
6. **Commit and push after every working step**, including its notes, with
   a plain message. GitHub is the source of truth and the backup. Confirm
   the push: a step that is not pushed is not saved there.

## Debugging

- Change one thing at a time; say what you expect before trying it.
- Read the real error and output. Check the project's `PITFALLS.md` first.
- After three failed tries on the same problem, stop trying fixes. List
  what is known, what is unknown, and the next check that will tell us more.

## Libraries and facts

Check current official docs or examples before using a fact or API you are
unsure of. Pin dependency versions in the project's usual version or lock
file so the same setup can be used again.

## Working style

- Use `plan-project` for anything bigger than an afternoon. Money, safety,
  installs, purpose and deleting unsaved work need the person's say.
- Use `check` before ending a feature; it explains when a reviewer can be skipped.
- Helpers follow `MODELS.md`: `maker-engineer` builds tickets,
  `maker-checker` reviews, `maker-researcher` finds facts.
- Read `~/.claude/maker-kit/knowledge/claude-pitfalls.md` once per project.
- **Electronics in any project** (boards, wiring, batteries, motors,
  anything mains-powered): use `~/.claude/maker-kit/packs/hardware/`. Put its
  `CLAUDE.md` in the project, and run its `SETUP.md` the first time this Mac
  needs it (`pio --version` fails). Its safety rules always apply.
- Offer one recommendation with one line of why.
- Corrections to how you work go in "Our own rules" in
  `~/.claude/CLAUDE.md`, keeping the rules already there.

<!-- cy-maker-kit:end -->

## Our own rules

(Add lessons here as you go.)
