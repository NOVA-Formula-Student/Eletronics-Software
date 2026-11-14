#include "pins.h"

constexpr uint32_t BLINK_HALF_PERIOD_MS = 125;  // 4 Hz, duty 50%
constexpr uint32_t DEBOUNCE_MS = 30;

// --- debounce ---
bool stableLevel = HIGH;      // com pull-up: solto = HIGH
bool lastReading = HIGH;
uint32_t lastChangeMs = 0;

// --- piscar ---
bool redLevel = false;
uint32_t lastToggleMs = 0;

// true se o botao "TS ativo" esta premido (leitura ja filtrada)
bool tsButtonPressed() {
  bool reading = digitalRead(PIN_TS_BUTTON);
  if (reading != lastReading) {
    lastChangeMs = millis();
    lastReading = reading;
  }
  if (millis() - lastChangeMs >= DEBOUNCE_MS) {
    stableLevel = reading;
  }
  return stableLevel == LOW;  // premido = LOW
}

void setup() {
  pinMode(PIN_TS_BUTTON, INPUT_PULLUP);
  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
}

void loop() {
  if (tsButtonPressed()) {
    digitalWrite(PIN_LED_GREEN, LOW);
    if (millis() - lastToggleMs >= BLINK_HALF_PERIOD_MS) {
      lastToggleMs = millis();
      redLevel = !redLevel;
      digitalWrite(PIN_LED_RED, redLevel ? HIGH : LOW);
    }
  } else {
    redLevel = false;
    digitalWrite(PIN_LED_RED, LOW);
    digitalWrite(PIN_LED_GREEN, HIGH);
  }
}