---
name: hw-debug
description: Electronics projects only (a folder with platformio.ini or WIRING.md). Step-by-step hardware debugging for ESP32/Arduino - nothing on serial, upload fails, resets, sensor not found, garbage output. USE WHEN the board misbehaves (no serial output, upload fails, resets, a sensor is not found, garbage output).
---
# Hardware debug, outside in

Ask for a photo of the wiring when anything physical is involved. Go in this
order and stop at the first failure:

1. **Power and cable.** Board LED on? Data cable (try another)? Port appears
   in `pio device list` when plugged, disappears when unplugged?
2. **Right board and speed.** `board =` matches the real board; monitor at
   115200 (garbage text = wrong speed, or the ESP32 ROM's own boot chatter,
   which is normal for a moment after reset).
   Native-USB boards (S3, C3, C6, XIAO): no output at all usually means the
   `-DARDUINO_USB_CDC_ON_BOOT=1` build flag is missing, or the port changed
   name after reset (list ports again).
3. **Code runs at all.** Flash the template untouched. Blink + SELFTEST PASS?
   If yes, the problem is in the new part or code, not the setup.
4. **Resets in a loop** ("rst:0x..", "Brownout detector"): power. Weak USB
   port or cable, or a load (servo, LEDs) drawing from the 3.3 V pin. Give the
   load its own supply, shared ground.
   "Guru Meditation" / backtrace: a crash. Decode it:
   `monitor_filters = esp32_exception_decoder` in platformio.ini.
5. **Part not found.** I2C: write a 10-line I2C scan in `selfTest()` (loop
   addresses 1-126 with `Wire.beginTransmission`/`endTransmission`, print each
   that answers 0), expect the address from
   the datasheet; check SDA/SCL pins for this board, pull-ups (most modules
   have them), 3.3 V vs 5 V module. One-wire/DHT: pull-up resistor.
6. **Pin problems.** Check the pin against `esp32-pitfalls.md` (boot pins,
   input-only pins, ADC2 with Wi-Fi, flash pins).
7. **Ground.** Every supply and every module shares GND with the board.
8. **Measure.** If they have a multimeter: voltage at the module's VCC and
   GND (powered), then continuity of each wire (power OFF). Guide them probe
   by probe.

Write what fixed it in the project's `PITFALLS.md`.
