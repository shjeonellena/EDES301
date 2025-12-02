#!/usr/bin/env python3

"""
HexaForm Actuator Init Test (Keyboard Version)
"""

import time
import Adafruit_BBIO.GPIO as GPIO


class ActuatorTest:
    """Test pump and solenoid valves using keyboard input."""

    def __init__(
        self,
        pump_pin="P2_2",   # air pump → ULN #1 IN1
        sol1_pin="P2_4",   # solenoid valve 1 → ULN #2 IN1
        sol2_pin="P2_6"    # solenoid valve 2 → ULN #2 IN2
    ):
        self.pump_pin = pump_pin
        self.sol1_pin = sol1_pin
        self.sol2_pin = sol2_pin

        self._setup()

    # ------------------------------------------------------------------
    def _setup(self):
        """Configure GPIO pins"""

        # Setup outputs
        GPIO.setup(self.pump_pin, GPIO.OUT)
        GPIO.setup(self.sol1_pin, GPIO.OUT)
        GPIO.setup(self.sol2_pin, GPIO.OUT)

        # Make sure everything starts OFF
        self._pump_off()
        self._sol1_off()
        self._sol2_off()

    # ------------------------------------------------------------------
    # Device control methods
    # ------------------------------------------------------------------

    def _pump_on(self):
        print("Pump ON")
        GPIO.output(self.pump_pin, GPIO.HIGH)

    def _pump_off(self):
        print("Pump OFF")
        GPIO.output(self.pump_pin, GPIO.LOW)

    def _sol1_on(self):
        print("Solenoid 1 ON")
        GPIO.output(self.sol1_pin, GPIO.HIGH)

    def _sol1_off(self):
        print("Solenoid 1 OFF")
        GPIO.output(self.sol1_pin, GPIO.LOW)

    def _sol2_on(self):
        print("Solenoid 2 ON")
        GPIO.output(self.sol2_pin, GPIO.HIGH)

    def _sol2_off(self):
        print("Solenoid 2 OFF")
        GPIO.output(self.sol2_pin, GPIO.LOW)

    # ------------------------------------------------------------------
    def run(self):
        print("\nActuator Keyboard Test Running")
        print("---------------------------------")
        print("Commands:")
        print("  1 → Pump ON")
        print("  2 → Pump OFF")
        print("  3 → Solenoid 1 ON")
        print("  4 → Solenoid 1 OFF")
        print("  5 → Solenoid 2 ON")
        print("  6 → Solenoid 2 OFF")
        print("  q → Quit")
        print("---------------------------------\n")

        while True:
            cmd = input("Enter command: ").strip().lower()

            if cmd == "1":
                self._pump_on()
            elif cmd == "2":
                self._pump_off()
            elif cmd == "3":
                self._sol1_on()
            elif cmd == "4":
                self._sol1_off()
            elif cmd == "5":
                self._sol2_on()
            elif cmd == "6":
                self._sol2_off()
            elif cmd == "q":
                print("Quitting.")
                break
            else:
                print("Invalid input.")

            time.sleep(0.1)

    # ------------------------------------------------------------------
    def cleanup(self):
        print("Cleaning up...")
        self._pump_off()
        self._sol1_off()
        self._sol2_off()
        GPIO.cleanup()

# ------------------------------------------------------------------------

if __name__ == '__main__':
    print("Program Start: Actuator Keyboard Test")

    test = ActuatorTest()

    try:
        test.run()
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        test.cleanup()
        print("Program Complete")
