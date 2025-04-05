import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

plus_pin = 4

GPIO.setup(plus_pin, GPIO.OUT)

try:
     GPIO.output(plus_pin, 1)
     time.sleep(5)
     GPIO.output(plus_pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
