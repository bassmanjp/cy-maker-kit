# Hardware pack (ESP32, Arduino and friends)

These rules apply to hardware projects, alongside the universal rules in
`~/.claude/CLAUDE.md`. Keep this file in the project's root as `CLAUDE.md`.
The safety rules below win over other working habits.

## Before touching hardware

- Read `~/.claude/maker-kit/knowledge/esp32-pitfalls.md` or
  `arduino-pitfalls.md` before touching pins, and `power-and-wiring.md`
  before motors, LED strips, relays or anything above 3.3 V.
- Ask for the exact board name. Boards with the same chip can have different
  pins; trust the maker's pinout drawing over a generic one.
- **Wiring first, on paper.** Before code uses a pin, write a table in
  `WIRING.md` (part pin → board pin, voltage, resistor). Run `wiring-check`,
  then have the person confirm the physical wiring matches, ideally with a photo.
- Add one sensor, output or behaviour at a time, never two new parts at once.

## Build and check

- Pure logic belongs in `lib/logic/`, without `Arduino.h`, with unit tests
  in `test/`. Hardware code in `src/` stays thin.
- Run `pio test -e native`, then `pio run -e board`. Use the actual board
  environment if it has a different name (for example `-e uno`).
- Upload with `flash` and read the serial output yourself. At boot the board
  must print `SELFTEST PASS` or `SELFTEST FAIL <why>`; add a self-test for
  each new part. Optional Wokwi simulation helps try ideas before buying parts.
- Done means the serial output or the person's eyes confirm the planned
  check on the real board. Say what you could not check.
- Check current library examples and pin versions in `platformio.ini`
  (`lib_deps = author/name@^1.2.3`).

## Debugging

Read the actual serial output and the project's `PITFALLS.md`, then the
relevant knowledge files. After three failed tries, stop, list known facts
and use `hw-debug` from the top. A charge-only cable, wrong board setting,
missing ground or wrong pin is often the cause.

## Safety (always)

- ESP32 pins are 3.3 V and about 12 mA. 5 V on a pin can kill the chip.
  Anything that runs at 5 V or more, or draws real current (motors, relays,
  LED strips, solenoids, pumps) needs a driver (transistor, MOSFET, driver
  board) and its own supply with a shared ground. Ask before wiring it.
- Never mains voltage (wall power) in a project. To switch a wall-powered
  thing, use a certified smart plug or switch that home-automation software
  can control, not a relay module on mains.
- Lithium batteries: protected cells and a proper charger board only.
- Unplug USB before rewiring.
