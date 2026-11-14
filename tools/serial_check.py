#!/usr/bin/env python3
"""Reset the board, print what it says, and pass when an expected line appears.

  uv run --with pyserial python serial_check.py --port /dev/cu.usbserial-0001 --expect "SELFTEST PASS"
  uv run --with pyserial python serial_check.py --port COM5 --seconds 20      (just watch)
Exit 0: expected line seen (or watch finished). 1: FAIL line or timeout. 2: port problem.
"""
import argparse, sys, time

# Windows pipes default to the ANSI code page; stray serial bytes would crash print().
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

try:
    import serial  # type: ignore
except ImportError:
    print("needs pyserial: run with `uv run --with pyserial python serial_check.py ...`")
    sys.exit(2)

ap = argparse.ArgumentParser()
ap.add_argument("--port", required=True)
ap.add_argument("--baud", type=int, default=115200)
ap.add_argument("--expect", help="line text that means success")
ap.add_argument("--fail", default="SELFTEST FAIL", help="line text that means failure")
ap.add_argument("--timeout", type=float, default=15)
ap.add_argument("--seconds", type=float, help="watch mode: just print for this long")
ap.add_argument("--no-reset", action="store_true")
a = ap.parse_args()

try:
    s = serial.Serial(a.port, a.baud, timeout=0.2)
except serial.SerialException as e:
    print(f"cannot open {a.port}: {e}\n(busy? another monitor open? wrong port? Linux: dialout group)")
    sys.exit(2)

if not a.no_reset:
    # Pulse EN via RTS with IO0 (DTR) released: normal boot, not download mode.
    try:
        s.dtr = False
        s.rts = True
        time.sleep(0.1)
        s.rts = False
    except (OSError, serial.SerialException):
        print("(this adapter cannot reset the board: press EN/RESET now)")

limit = a.seconds if a.seconds else a.timeout
end = time.time() + limit
buf = b""
while time.time() < end:
    try:
        chunk = s.read(256)
    except serial.SerialException:
        time.sleep(0.5)  # native-USB boards drop the port while resetting
        try:
            s.close(); s = serial.Serial(a.port, a.baud, timeout=0.2)
        except serial.SerialException:
            pass
        continue
    if not chunk:
        continue
    buf += chunk
    while b"\n" in buf:
        line, buf = buf.split(b"\n", 1)
        text = line.decode("utf-8", "replace").rstrip("\r")
        print(text)
        if a.seconds:
            continue
        if a.fail and a.fail in text:
            print(f"\nFAIL: board reported '{text}'")
            sys.exit(1)
        if a.expect and a.expect in text:
            print(f"\nPASS: saw '{a.expect}'")
            sys.exit(0)

if a.seconds:
    sys.exit(0)
print(f"\nFAIL: no '{a.expect}' within {limit:.0f} s (nothing printed = wrong baud, no code running, or native USB needs ARDUINO_USB_CDC_ON_BOOT=1;\n some boards cannot be reset over USB: rerun with --no-reset and press the EN/RESET button)")
sys.exit(1)
