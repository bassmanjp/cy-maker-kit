#include <unity.h>
#include "debounce.h"

void setUp() {}
void tearDown() {}

void test_bounce_is_ignored() {
  Debouncer d(30);
  TEST_ASSERT_FALSE(d.update(true, 0));
  TEST_ASSERT_FALSE(d.update(false, 5));   // bounce
  TEST_ASSERT_FALSE(d.update(true, 10));
  TEST_ASSERT_FALSE(d.update(true, 25));   // not stable long enough
  TEST_ASSERT_TRUE(d.update(true, 41));    // stable 31 ms: one press
  TEST_ASSERT_FALSE(d.update(true, 100));  // held: no repeat
}

void test_release_then_press_again() {
  Debouncer d(30);
  d.update(true, 0);
  TEST_ASSERT_TRUE(d.update(true, 30));
  d.update(false, 50);
  TEST_ASSERT_FALSE(d.update(false, 90));  // release is not a press
  TEST_ASSERT_FALSE(d.isPressed());
  d.update(true, 100);
  TEST_ASSERT_TRUE(d.update(true, 130));
}

void test_millis_wraparound() {
  Debouncer d(30);
  d.update(true, 0xFFFFFFF0u);
  TEST_ASSERT_TRUE(d.update(true, 0x0000000Fu));  // 31 ms later, across wrap
}

void test_moving_average() {
  MovingAverage<4> avg;
  TEST_ASSERT_EQUAL_FLOAT(10.0f, avg.add(10));
  TEST_ASSERT_EQUAL_FLOAT(15.0f, avg.add(20));
  avg.add(30);
  TEST_ASSERT_EQUAL_FLOAT(25.0f, avg.add(40));
  TEST_ASSERT_EQUAL_FLOAT(35.0f, avg.add(50));  // oldest (10) dropped
}

int main() {
  UNITY_BEGIN();
  RUN_TEST(test_bounce_is_ignored);
  RUN_TEST(test_release_then_press_again);
  RUN_TEST(test_millis_wraparound);
  RUN_TEST(test_moving_average);
  return UNITY_END();
}
