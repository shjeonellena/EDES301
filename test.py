import Adafruit_BBIO.GPIO as GPIO
import time

pin = "P2_6"
GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, GPIO.HIGH)
    print("ON")
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    print("OFF")
    time.sleep(1)
