# Power and wiring basics

## Driving loads
- LED: resistor in series. (Supply - LED voltage) / current. 3.3 V, red LED,
  10 mA: (3.3-2.0)/0.01 = 130 ohm, use 220 ohm.
- Motor, relay coil, solenoid, pump, buzzer > 12 mA: logic-level N-MOSFET
  (e.g. AO3400, IRLZ44N) or NPN transistor (2N2222 + 1k base resistor), low
  side; flyback diode (1N4007/1N5819) across coils and motors, stripe to +.
- MOSFET loads: 10k resistor from gate to GND, so the load stays off while
  the board boots (pins float during reset).
- Relay modules (low-voltage loads only): many 5 V boards stay switched on
  with a 3.3 V signal. Use one rated for 3.3 V input, one with a separate
  JD-VCC jumper wired per its docs, or drive it through a transistor.
- Servos: own 5-6 V supply (stalls draw 1 A+), signal from GPIO, shared GND.
- WS2812/NeoPixel strips: 60 mA per LED at full white. 5 V supply sized for
  it, 300-500 ohm resistor on data, 1000 uF cap at the strip, level shift the
  data line from an ESP32 (74AHCT125) for any strip powered at 5 V.
- Steppers: driver board (A4988, TMC2209), never direct.

## Reading things
- Button: `INPUT_PULLUP`, button to GND, reads LOW when pressed; debounce
  (the template's `Debouncer`).
- 5 V signal into ESP32: divider 10k (top) / 20k (bottom) gives 3.3 V.
- I2C: SDA/SCL, pull-ups 4.7k to 3.3 V if the module has none; one address
  per device on a bus; keep wires short.
- Analog sensors: power them from 3.3 V so they can't exceed the ADC range.

## Supplies
- Every supply shares GND with the board.
- USB port: about 500 mA. Plan anything bigger with its own supply.
- Batteries: protected 18650 or LiPo + TP4056 (with protection) charger
  board; a buck or LDO to 3.3 V. Never charge unprotected cells.
- LiPo plugs (JST): red/black order differs between makers. Check the
  board's + and - marks against the battery's wires before plugging in.
- Never feed the board's 5V/VIN pin from another supply while USB is plugged
  in, unless the board has a diode there (check the schematic).
- Mains (wall power): never in a project. Certified smart plugs or switches.

## Breadboard habits
- Unplug USB before changing wires.
- Red = +, black = GND, keep it consistent.
- Photo the board when it works; it is your undo.
- Continuity and resistance checks with the multimeter: power OFF.
- Boards with no USB port (ESP32-CAM, bare modules) need a USB-serial
  adapter, and IO0 tied to GND while uploading.
