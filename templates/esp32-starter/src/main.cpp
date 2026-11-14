#include <Arduino.h>
#include "debounce.h"

// The board's own LED. Picked automatically; override in platformio.ini with
// build_flags = -DLED_PIN=8 (for example the ESP32-C3 SuperMini's plain LED).
// On boards with an RGB LED (S3 DevKitC, C3 DevKitM, C6 DevKitC) the core's
// RGB_BUILTIN makes digitalWrite light it white.
#ifndef LED_PIN
  #if defined(RGB_BUILTIN)
    #define LED_PIN RGB_BUILTIN
  #elif defined(LED_BUILTIN)
    #define LED_PIN LED_BUILTIN
  #else
    #define LED_PIN 2  // most classic ESP32 DevKits
  #endif
#endif

// The board's BOOT button: GPIO 0 on classic ESP32 and S3, GPIO 9 on C3/C6.
// Arduino Uno/Nano have none: wire a button from pin 2 to GND.
#ifndef BUTTON_PIN
  #if defined(ARDUINO_ARCH_AVR)
    #define BUTTON_PIN 2
  #elif defined(CONFIG_IDF_TARGET_ESP32C3) || defined(CONFIG_IDF_TARGET_ESP32C6) || defined(CONFIG_IDF_TARGET_ESP32H2)
    #define BUTTON_PIN 9
  #else
    #define BUTTON_PIN 0
  #endif
#endif

Debouncer button;
uint32_t lastBlink = 0;
bool ledOn = false;
uint32_t blinkMs = 500;

// Check what can be checked at boot. Add one check per new part.
// The flash skill waits for "SELFTEST PASS".
bool selfTest() {
  bool ok = true;
  // Example for an I2C sensor (add #include <Wire.h> at the top):
  // Wire.begin();
  // Wire.beginTransmission(0x76);
  // if (Wire.endTransmission() != 0) { Serial.println("SELFTEST FAIL bme280 not found at 0x76"); ok = false; }
  return ok;
}

void setup() {
  Serial.begin(115200);
  uint32_t start = millis();
  while (!Serial && millis() - start < 2000) {}  // native-USB boards
  delay(200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.println();
  Serial.println(F("BOOT starter"));
  Serial.print(F("LED pin "));
  Serial.print(LED_PIN);
  Serial.print(F(", button pin "));
  Serial.println(BUTTON_PIN);
  Serial.println(selfTest() ? F("SELFTEST PASS") : F("SELFTEST FAIL"));
}

void loop() {
  uint32_t now = millis();
  if (button.update(digitalRead(BUTTON_PIN) == LOW, now)) {
    blinkMs = (blinkMs == 500) ? 100 : 500;
    Serial.print(F("button: blink every "));
    Serial.print((unsigned long)blinkMs);
    Serial.println(F(" ms"));
  }
  if (now - lastBlink >= blinkMs) {
    lastBlink = now;
    ledOn = !ledOn;
    digitalWrite(LED_PIN, ledOn ? HIGH : LOW);
  }
}
