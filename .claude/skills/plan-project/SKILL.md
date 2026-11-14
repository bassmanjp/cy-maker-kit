---
name: plan-project
description: Plan any project or big feature before building - goal, proof it works, tools, small steps and an independent review. USE WHEN starting anything bigger than an afternoon, adding a subsystem, or when the person says plan the project.
---
# Plan before building

1. **Aim.** Use `be-ambitious` briefly: what is this really for, and what
   would an expert do?
2. **Ground truth first.** Read the project's `CLAUDE.md`, notes and files
   to understand its tools. List unchecked assumptions (a service's limits,
   a file format, a library's API) and check them now. Use
   `maker-researcher` if it takes reading.
3. Write `PLAN.md`:
   - Goal in the person's words, and the check that proves it works in real use.
   - Tools, materials or sources needed; costs only where relevant.
   - Small steps, each with its own test or practical check.
   - Risks: what breaks if a key assumption is wrong, including secrets,
     backups and saved data where relevant.
   - One approach not tried before, and why it is in or out.
   - **For hardware only:** exact board and parts, links and prices, what
     they already have, wiring table for `WIRING.md`, power budget and
     checks on the real board. Read the hardware pack and relevant pitfalls.
4. **Review.** Send `PLAN.md` to `maker-checker`: check missing
   requirements, wrong assumptions and steps without a real check. Check
   secrets and data loss for software, wiring and power for hardware.
   Fix real findings. Two review rounds at most; safety and other blocking
   findings must still be resolved.
5. Show the person the short version (goal, any cost, steps) with one
   recommendation. Money and safety choices are theirs; the rest you decide.
