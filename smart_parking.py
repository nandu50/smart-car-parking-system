import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for IR sensors and LEDs
sensor1_pin = 17
sensor2_pin = 18
led1_pin = 23
led2_pin = 24

# Setup GPIO pins
GPIO.setup(sensor1_pin, GPIO.IN)
GPIO.setup(sensor2_pin, GPIO.IN)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

try:
    while True:
        # Read sensor status
        sensor1_status = GPIO.input(sensor1_pin)
        sensor2_status = GPIO.input(sensor2_pin)

        # Update LED status based on sensor 1
        if sensor1_status == GPIO.LOW:
            GPIO.output(led1_pin, GPIO.HIGH)
            print("Slot 1 occupied")
        else:
            GPIO.output(led1_pin, GPIO.LOW)
            print("Slot 1 is available")

        # Update LED status based on sensor 2
        if sensor2_status == GPIO.LOW:
            GPIO.output(led2_pin, GPIO.HIGH)
            print("Slot 2 occupied")
        else:
            GPIO.output(led2_pin, GPIO.LOW)
            print("Slot 2 is available")

        # Delay for stability
        time.sleep(5)

except KeyboardInterrupt:
    # Clean up GPIO
    GPIO.cleanup()