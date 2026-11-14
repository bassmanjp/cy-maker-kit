// Pure logic: no Arduino.h here, so it can be tested on the computer.
#pragma once
#include <stdint.h>  // not <cstdint>: AVR has no C++ standard library

// Turns a noisy button reading into clean presses.
class Debouncer {
 public:
  explicit Debouncer(uint32_t stableMs = 30) : stableMs_(stableMs) {}

  // Feed the raw reading and the current time (millis()).
  // Returns true exactly once per press (stable change from up to down).
  bool update(bool pressedRaw, uint32_t nowMs) {
    if (pressedRaw != lastRaw_) {
      lastRaw_ = pressedRaw;
      changedAt_ = nowMs;
    }
    if ((nowMs - changedAt_) >= stableMs_ && pressedRaw != stable_) {
      stable_ = pressedRaw;
      return stable_;
    }
    return false;
  }

  bool isPressed() const { return stable_; }

 private:
  uint32_t stableMs_;
  uint32_t changedAt_ = 0;
  bool lastRaw_ = false;
  bool stable_ = false;
};

// Running average over the last N readings (for noisy ADC values).
template <int N>
class MovingAverage {
 public:
  float add(float v) {
    sum_ += v - buf_[i_];
    buf_[i_] = v;
    i_ = (i_ + 1) % N;
    if (count_ < N) count_++;
    return sum_ / count_;
  }
 private:
  float buf_[N] = {};
  float sum_ = 0;
  int i_ = 0;
  int count_ = 0;
};
