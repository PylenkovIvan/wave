import RPi.GPIO as GPIO

pin = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN)

try:
    while True:
        print(GPIO.input(pin))
finally:
    GPIO.output(pin, 0)
    GPIO.cleanup()