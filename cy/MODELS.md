# Which model does what

Claude Code lets the main session hand jobs to helpers, each on its own
model and effort. Picking well saves most of your usage at no loss of
quality. The kit installs three helpers in `~/.claude/agents/`.

**On a Pro (smaller) plan:** main session on Sonnet at effort medium, and set
`effort: high` in `maker-engineer.md` and `maker-checker.md`. Use helpers
less: on the same model they save context, not usage. **On a Max plan:**
Opus for the main session, helpers as shipped.

| Who | Model | Effort | Does |
|-----|-------|--------|------|
| You + main session | the strongest on your plan (Opus; Sonnet on a small plan) | high | plans, judges, talks to you, solves problems across the project |
| `maker-engineer` | Sonnet | xhigh | a well-defined job: make files, run checks, commit |
| `maker-checker` | Sonnet | xhigh | independent review of finished work or a plan; never edits |
| `maker-researcher` | Sonnet | medium | reads docs and source material (datasheets for hardware); reports with sources |
| lookups | Haiku (or inline) | low | one quick fact |

## Rules
- **The main session thinks, helpers do.** Planning, unclear asks and
  "why is this behaving strangely" stay in the main session. A job longer than
  about 15 steps with a clear finish line goes to `maker-engineer`.
- **Settle unknowns before handing off.** A helper gets a ticket, not a
  puzzle.
- **Never a stronger model as a helper** than the main session.
- **Effort matches the job.** Lookups low, building and checking xhigh;
  max only for the one retry after a failed check.
  Don't run everything at max; it burns the week's usage for nothing.
- **Judge helpers by the tests and the diff, never by their report.**
- **Step up on failure, once:** a failed check goes to a fresh helper with
  the failure attached at effort max. Fails again: the main session does it.
- **Parallel only when independent.** Two helpers never edit the same files.

## The ticket every helper gets
```
TASK: <short name, same for every attempt>
GOAL: <one sentence>
FILES: <about five>
DONE WHEN: <a command or check that proves it>
BUDGET: <about 60 steps>
ATTEMPT: 1
```
End every brief with: "If a tool or permission check refuses something,
stop and report it; never work around it. Hand back DONE / LEFT / TESTS /
COMMITS."

## Usage
Check your plan's usage now and then (the app's usage page). Long
conversations and high effort use the most. Every helper adds its own
usage; running them in parallel only saves time.
Start a fresh session for a new task instead of one endless thread.

## If you also pay for ChatGPT
OpenAI's Codex CLI makes a good second reviewer that doesn't share Claude's
blind spots. Optional: have the main session run `codex exec` with the diff
and the goal, and weigh its findings like the checker's.
