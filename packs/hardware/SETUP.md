# Hardware setup (electronics projects only)

Part of the kit's setup wizard; Claude runs it when the first project is
electronics, or later the first time a project needs a board.

## Build tools

PlatformIO turns code into something the board runs and uploads it.

- **uv** (installs Python tools cleanly), if `uv --version` fails:
  `curl -LsSf https://astral.sh/uv/install.sh | sh`
  (Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`).
- **PlatformIO:** `uv tool install platformio`, then `pio --version`.
- Run `uv run --with pyserial python ~/.claude/maker-kit/tools/doctor.py`
  (during setup: `KIT/tools/doctor.py`). Every line should be OK except the
  board line until the board is plugged in.

## Plug in the board

Ask them which board they have (name printed on it or the shop listing) and
to plug it in with a USB cable that carries **data** (many cables only
charge: the number one first-day problem). On a Mac, if a pop-up asks to
allow the accessory, they click Allow. Run the doctor again and find the new
port (`/dev/cu.usbserial-*`, `/dev/cu.wchusbserial*` or `/dev/cu.usbmodem*`;
use the `cu.` name). No port with a CP2102/CH340 board on an older macOS:
install the maker's driver. Unknown board: `uv run --with esptool esptool chip-id`.

## First blink

In a project made from `templates/esp32-starter/` with the board set:

1. `pio test -e native`: the logic tests run on the computer, no board.
2. `pio run -e board`: it builds. The first build downloads the ESP32
   toolchain (several hundred MB, a few minutes): run it in the background or
   with a long timeout and tell them it is a one-time wait.
3. `flash` skill: upload, then `serial_check.py` waits for `SELFTEST PASS`.
   The board prints which LED pin it uses. If it has an onboard LED (plain or
   RGB), it should blink: ask them to look. Boards with only a power LED:
   SELFTEST PASS is the check.
