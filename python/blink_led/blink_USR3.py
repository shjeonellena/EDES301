#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3 LED
--------------------------------------------------------------------------
License:   
Copyright 2025 - Ellena Jeon

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
   this list of conditions and the following disclaimer in the documentation 
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
   may be used to endorse or promote products derived from this software 
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple program that blinks the onboard BeagleBone USR3 LED at 5 Hz 
(5 on/off cycles per second, or 10 toggles per second).

References:
  - Adafruit_BBIO library documentation:
    https://github.com/adafruit/adafruit-beaglebone-io-python
--------------------------------------------------------------------------
"""

import Adafruit_BBIO.GPIO as GPIO
import time

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------
LED = "USR3"        # Onboard blue LED
FREQ = 5.0          # Blink frequency in Hz (full on/off cycles per second)
PERIOD = 1.0 / FREQ # Time for one full cycle = 0.2 s
HALF_PERIOD = PERIOD / 2.0  # LED on or off duration = 0.1 s

# ------------------------------------------------------------------------
# Main Program
# ------------------------------------------------------------------------
def main():
    """Blink the onboard USR3 LED at 5 Hz until interrupted."""
    GPIO.setup(LED, GPIO.OUT)
    print("Blinking USR3 LED at 5 Hz... Press Ctrl+C to stop.")

    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(HALF_PERIOD)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(HALF_PERIOD)
    except KeyboardInterrupt:
        print("\nExiting and cleaning up...")
    finally:
        GPIO.cleanup()

# ------------------------------------------------------------------------
# Script Entry Point
# ------------------------------------------------------------------------
if __name__ == "__main__":
    main()
