---
name: wiring-check
description: Electronics projects only (a folder with platformio.ini or WIRING.md). Check a wiring plan before anything is connected - voltage levels, current, boot pins, shared ground, resistors. USE WHEN adding an electronic part to a circuit, before wiring, when reviewing WIRING.md, or when a photo of a breadboard is shared.
---
# Wiring check

For each row of `WIRING.md` (part pin → board pin), check and report a short
table with OK / FIX and why:

- **Voltage**: part's logic level vs board (ESP32 = 3.3 V, Uno = 5 V). A 5 V
  output into an ESP32 pin needs a divider or level shifter.
- **Current**: an ESP32 pin drives an LED with a resistor (220-1k ohm), never a
  motor, relay coil, buzzer over ~12 mA or a strip. Those need a transistor or
  driver, plus a flyback diode for coils.
- **Pin choice**: against `esp32-pitfalls.md` (boot strapping pins, input-only
  34-39, flash pins 6-11, ADC2 and Wi-Fi, the board's own LED/USB pins).
- **Power budget**: add up the current of every part; USB gives about 500 mA,
  the 3.3 V regulator on many boards 500-800 mA at best. Servos, motors and
  LED strips get their own supply.
- **Shared ground** between every supply.
- **Pull-ups/pull-downs** needed (buttons, I2C, one-wire), and whether the
  module already has them.
- **Polarity**: LEDs, electrolytic capacitors, diodes, sensors that die
  reversed.

Only after every row is OK do you tell them to wire it. Then ask for a photo
and compare it to the table.
