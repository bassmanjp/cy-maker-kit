---
name: test
description: Find and run the project's tests, add useful checks for changed behaviour, and confirm the result in real use. USE WHEN testing a project, adding logic, fixing a bug, or before committing working changes.
---
# Test the project you are in

Read the project's `CLAUDE.md` for its test commands first. Look at the
files to find the stack; do not assume a board or a programming language.
For a project with several parts, test each part you changed.

- **`platformio.ini`:** run `pio test -e native`. Keep pure logic in
  `lib/logic/`, without `Arduino.h`, with tests in `test/`. The project's
  hardware rules cover building, simulation and the on-board self-test;
  use `flash` for the real board check.
- **`package.json`:** read its `scripts.test` and `packageManager` field,
  then the lockfile. If neither names a manager, use npm.
  Use the matching manager: `npm test`,
  `pnpm run test`, `yarn test` or `bun run test`. Never use bare
  `bun test`. If these clues disagree, resolve that before installing
  anything. If there is no test script, say there are no tests yet and
  propose the smallest useful test.
- **`pyproject.toml`, pytest settings or Python tests:** read the project's
  setup and run `uv run pytest`, using its declared test dependency group
  if needed. If pytest or tests are missing, say so and propose the
  smallest useful test before adding anything.
  Ask before installing a new tool.
- **Another stack:** use its documented test command. If none exists,
  say "There are no tests yet" and propose the smallest useful one: a known
  input and expected output, a design measurement, or a short checklist
  for a piece of writing. Do not invent a passing test result.

Keep logic separate from screens, devices and outside services so it can
be tested on its own. Write a test before or with new logic; a bug fix gets
a test that would have caught it. Use the project's usual tools.

Run the relevant tests before each working commit and report the command
and result. Then check the actual app, script, printed part, automation or
finished writing against the goal. Automated tests alone do not prove the
real thing works.
