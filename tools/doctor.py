#!/usr/bin/env python3
"""Check this computer is ready for ESP32/Arduino work. Read-only: installs nothing."""
import platform, shutil, subprocess, sys, glob, os

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

ok_all = True

def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as e:  # noqa: BLE001
        return ""

def check(name, good, detail, fix=""):
    global ok_all
    mark = "OK  " if good else "MISS"
    print(f"[{mark}] {name}: {detail}")
    if not good:
        ok_all = False
        if fix:
            print(f"       fix: {fix}")

system = platform.system()
print(f"OS: {system} {platform.release()} ({platform.machine()})  Python {sys.version.split()[0]}")
in_wsl = "microsoft" in platform.release().lower()
if in_wsl:
    print("       note: WSL cannot see USB boards without usbipd; run the kit from Windows itself.")

gitv = run(["git", "--version"])
check("git", gitv.startswith("git version"), gitv or "not found",
      "Mac: xcode-select --install | Windows: https://git-scm.com | Linux: package manager")

uv = shutil.which("uv")
check("uv", bool(uv), run(["uv", "--version"]) or "not found", "https://docs.astral.sh/uv/ (install script)")

pio = shutil.which("pio") or shutil.which("platformio")
check("PlatformIO", bool(pio), run([pio, "--version"]) if pio else "not found", "uv tool install platformio")

cxx = shutil.which("g++") or shutil.which("clang++")
check("C++ compiler (for tests on the computer)", bool(cxx), cxx or "not found",
      "Mac: xcode-select --install | Windows: winget install -e --id BrechtSanders.WinLibs.POSIX.UCRT | Linux: build-essential")

# Serial ports
ports = []
try:
    from serial.tools import list_ports  # type: ignore
    ports = [(p.device, p.description, f"{p.vid:04x}:{p.pid:04x}" if p.vid else "") for p in list_ports.comports()]
except ImportError:
    if system == "Darwin":
        ports = [(p, "", "") for p in glob.glob("/dev/cu.usb*") + glob.glob("/dev/cu.wchusb*") + glob.glob("/dev/cu.SLAB*")]
    elif system == "Linux":
        ports = [(p, "", "") for p in glob.glob("/dev/ttyUSB*") + glob.glob("/dev/ttyACM*")]
    else:
        print("       (install pyserial to list Windows COM ports: run with `uv run --with pyserial python tools/doctor.py`)")

CHIPS = {"10c4:ea60": "CP210x", "1a86:7523": "CH340", "1a86:55d4": "CH9102", "303a:1001": "ESP32-S3/C3 native USB",
         "0403:6001": "FTDI", "2341:0043": "Arduino Uno", "2341:0001": "Arduino Uno", "2e8a:000a": "Raspberry Pi Pico"}
# Only USB serial devices (pyserial gives them a vendor id); skips built-in and Bluetooth ports.
usb_ports = [p for p in ports if (p[2] or not p[1]) and "bluetooth" not in (p[0] + p[1]).lower()
             and "debug-console" not in p[0] and "/dev/ttyS" not in p[0]]
if not usb_ports:
    print("[....] board on a serial port: none seen (fine until the board is plugged in)")
    print("       plug the board in with a DATA cable; no port with a CP2102/CH340 board = install its driver")
else:
  check("board on a serial port", True,
      ", ".join(f"{d} {CHIPS.get(v, desc)}".strip() for d, desc, v in usb_ports) or "none seen",
      "")

if system == "Linux" and usb_ports:
    groups = run(["id", "-nG"]).split()
    check("serial permission (dialout)", "dialout" in groups or "uucp" in groups, " ".join(groups),
          "sudo usermod -aG dialout $USER, then log out and in")

print()
print("READY" if ok_all else "NOT READY: fix the MISS lines, one at a time, then run again.")
sys.exit(0 if ok_all else 1)
