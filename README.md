# EDES301
EDES 301 Repository

# HexaForm Actuator 

This project provides a simple **keyboard-driven test interface** for the HexaForm prototype.  
Using a BeagleBone and GPIO control, you can:

- Turn an **air pump** on and off  
- Toggle **two solenoid valves** (Formation 1 and Formation 2)  
- See the current state and hints on a **16x2 HD44780 LCD** with an I²C backpack

It’s meant as a quick way to verify that wiring, drivers, and actuators are working as expected.

---

## Features

- Keyboard commands to control:
  - Pump (ON/OFF)
  - Solenoid 1 (Formation 1)
  - Solenoid 2 (Formation 2)
- Live status feedback on the HD44780 display:
  - Shows current action (e.g., `Pump ON`, `Formation 1`, `Turning off...`)
  - Shows which key to press to switch states (e.g., `OFF --> 2`)
- Safe shutdown:
  - Turns off all actuators
  - Clears the LCD and turns off the backlight
  - Calls `GPIO.cleanup()` on exit

---

## Hardware Overview

**Controller:**
- BeagleBone (e.g., BeagleBone Black / PocketBeagle)  
- GPIO pins used:
  - `P2_2` → Air pump (via ULN driver input)
  - `P2_4` → Solenoid 1 (via ULN driver input)
  - `P2_6` → Solenoid 2 (via ULN driver input)

**Actuation:**
- 1× Air pump
- 2× Solenoid valves  
- 1× ULN transistor array / driver (e.g., ULN2803A or similar) between GPIO and actuators
- External power supply for pump and solenoids (do **not** power them directly from the BeagleBone pins)

**Display:**
- HD44780-compatible 16x2 character LCD
- I²C backpack (e.g., PCF8574T)
- Connected to I²C bus on the BeagleBone
- Controlled via the `hd44780` CircuitPython-style library

---

## Software Requirements

On the BeagleBone:

- Python 3
- [`Adafruit_BBIO`](https://github.com/adafruit/adafruit-beaglebone-io-python) for GPIO
- `hd44780` (https://github.com/bablokb/circuitpython-hd44780/tree/master) library for controlling the LCD (the one used in:
  ```python
  import hd44780
  display = hd44780.HD44780()
  ```)

Make sure these are installed and importable in Python before running the script.

---

## File

The main script (for example):

```bash
actuator_keyboard_test.py
