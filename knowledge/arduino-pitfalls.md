# Arduino (AVR: Uno, Nano, Mega) pitfalls

- 5 V logic. A 3.3 V module (most sensors sold for ESP32, SD cards, many
  displays) may need a level shifter on its inputs.
- Uno/Nano: 2 KB RAM. Long strings eat it: wrap text in `F("...")`.
  "Random" resets or garbage after adding code = out of RAM.
- Pins 0 and 1 are the USB serial; using them breaks upload and Serial.
- Clone Nanos: old bootloader (`board = nanoatmega328`) and CH340 USB chip
  (driver on Windows / older macOS).
- Pin 13 has the onboard LED: it flickers at boot.
- `analogWrite` (PWM) only on pins marked `~` (3, 5, 6, 9, 10, 11 on Uno).
- Interrupts: only pins 2 and 3 on Uno/Nano. Variables shared with an
  interrupt must be `volatile`.
- 40 mA per pin absolute max, 20 mA sensible, 200 mA whole chip.
- `int` is 16 bits (max 32767): `millis()` must go in `unsigned long`.
- Servo library disables PWM on pins 9 and 10.
