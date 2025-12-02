#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for monochromatic character LCD on PocketBeagle (parallel 4-bit)."""

import time

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# PocketBeagle GPIO mapping (header pins P2_03..P2_08)
# RS  -> P2_03 -> GPIO23
# EN  -> P2_04 -> GPIO44
# D4  -> P2_05 -> GPIO26
# D5  -> P2_06 -> GPIO46
# D6  -> P2_07 -> GPIO27
# D7  -> P2_08 -> GPIO47

lcd_rs = digitalio.DigitalInOut(board.GPIO23)
lcd_en = digitalio.DigitalInOut(board.GPIO44)
lcd_d7 = digitalio.DigitalInOut(board.GPIO47)
lcd_d6 = digitalio.DigitalInOut(board.GPIO27)
lcd_d5 = digitalio.DigitalInOut(board.GPIO46)
lcd_d4 = digitalio.DigitalInOut(board.GPIO26)

for pin in (lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7):
    pin.direction = digitalio.Direction.OUTPUT

# Initialise the LCD class (no explicit backlight pin)
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en,
    lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

# If your backlight is wired to 5V directly, it will always be on.
# If it's on a GPIO transistor, you can control that separately.

# Print a two line message
lcd.clear()
lcd.message = "Hello\nPocketBeagle"
time.sleep(5)

# Print two line message right to left
lcd.clear()
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello\nPocketBeagle"
time.sleep(5)

# Return text direction to left to right
lcd.text_direction = lcd.LEFT_TO_RIGHT

# Display cursor
lcd.clear()
lcd.cursor = True
lcd.message = "Cursor! "
time.sleep(5)

# Display blinking cursor
lcd.clear()
lcd.blink = True
lcd.message = "Blinky Cursor!"
time.sleep(5)
lcd.blink = False
lcd.clear()

# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg

# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()

lcd.clear()
lcd.message = "Going to sleep\nCya later!"
time.sleep(3)

lcd.clear()
