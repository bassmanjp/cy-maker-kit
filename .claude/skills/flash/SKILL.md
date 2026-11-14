---
name: flash
description: Electronics projects only (a folder with platformio.ini or WIRING.md). Build, upload to the board and read its serial output to confirm it works. USE WHEN flashing a board, uploading firmware, or checking what the board prints over serial.
---
# Flash and check

1. `pio run -e board` (stop on error, fix it first). The very first build
   downloads the toolchain: run it in the background or with a long timeout.
2. Find the port: `pio device list`. More than one: ask which, or unplug and
   compare.
3. `pio run -e board -t upload --upload-port <port>`.
   - "Failed to connect" / "Wrong boot mode": ask them to hold BOOT, tap
     EN/RST, release BOOT, then upload again.
   - "Permission denied" (Linux): the user needs the `dialout` group.
   - Port busy: something else has it open (another serial monitor). Close it.
4. Check it: `uv run --with pyserial python ~/.claude/maker-kit/tools/serial_check.py --port <port> --expect "SELFTEST PASS" --timeout 15`
   It resets the board and prints everything it hears. Read that output.
   Board did not reset (some boards can't over USB): add `--no-reset` and ask
   them to press EN/RESET. Exit 0 means the expected line came; anything else is a failure: show
   the last lines and go to `hw-debug`.
5. For a longer look: the same tool with `--seconds 30` instead of `--expect`
   (an interactive monitor does not work from Claude's shell).
6. Say it works only when the output, or the person's eyes, confirm the check.
