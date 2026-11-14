# ESP32 pitfalls (classic ESP32 / WROOM-32 unless noted)

Check the exact board's pinout drawing; these are chip rules.

## Pins
- **Boot strapping pins: GPIO 0, 2, 5, 12, 15.** Their level at power-up picks
  the boot mode. A part that pulls them up or down can stop the board booting
  or uploading. GPIO 12 high at boot sets flash voltage wrong: board won't boot.
  Use them last, for outputs only.
- **GPIO 6-11 are the flash chip.** Never use them.
- **GPIO 34, 35, 36 (VP), 39 (VN) are input only**, no internal pull-up.
- **ADC2 pins (0, 2, 4, 12-15, 25-27) stop working while Wi-Fi is on.** Use
  ADC1 (32-39) for analog reads in Wi-Fi projects.
- ADC is non-linear near 0 V and 3.3 V and noisy: average several reads, use
  `analogReadMilliVolts()`, don't expect better than ~5%.
- GPIO 1 and 3 are the USB serial (TX/RX). Using them breaks Serial.
- Every output-capable pin can be PWM (not 34-39) (`ledcAttach` in core 3.x, `ledcSetup/ledcAttachPin`
  in 2.x; the template pins espressif32 8.x, which ships core 3.x).
- Pins are 3.3 V, about 12 mA safe (40 mA absolute max). **Not 5 V tolerant.**

## S3 / C3 / C6 (newer chips)
- Native USB: if Serial prints nothing, add
  `-DARDUINO_USB_CDC_ON_BOOT=1` and wait for `Serial` after `begin()`.
- The port may change name or vanish while it resets; re-list ports after upload.
- S3 strapping pins: 0, 3, 45, 46. C3: 2, 8, 9. Different again from classic.
- RGB onboard LED (S3 DevKitC: GPIO 48, or 38 on v1.1; C3/C6 DevKitC: 8):
  use `RGB_BUILTIN` / `rgbLedWrite()`, a plain `digitalWrite(48, ...)` stays dark.
- BOOT button: GPIO 0 on classic and S3, GPIO 9 on C3/C6.
- S3 boards with PSRAM (N8R8, N16R8) on octal PSRAM: GPIO 35-37 are taken.

## Power
- Brownout resets: Wi-Fi transmit draws ~300-500 mA spikes. Weak cable, long
  wire, or powering a servo from the board resets it. Put a 100-470 uF cap
  near 3V3/GND for battery builds.
- The board's 5 V / VIN pin is USB power, before the regulator; 3V3 pin is
  the regulator output: don't draw more than a few hundred mA from it.
- Deep sleep current depends on the board (USB chip and LEDs keep drawing);
  a bare DevKit rarely gets below several mA.

## Software
- `delay()` inside `loop()` blocks everything; use `millis()` timing for more
  than one thing at once.
- Watchdog resets ("Task watchdog got triggered"): a loop that never yields.
- Wi-Fi: 2.4 GHz only. Reconnect logic is needed; routers drop clients.
- Store Wi-Fi passwords in a `secrets.h` that is in `.gitignore`.
- `String` in long-running code fragments memory; prefer fixed buffers.
- Crash backtraces: `monitor_filters = esp32_exception_decoder`.
- ESPHome is the easy path when the goal is "a sensor/switch in Home
  Assistant": YAML, no C++. Use the Arduino/PlatformIO path when the logic
  is custom.
