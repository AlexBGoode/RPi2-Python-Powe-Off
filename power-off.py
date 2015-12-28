# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO

# Define a function to keep script running
def loop():
    raw_input()

# Define a function to run when an interrupt is called
def shutdown(pin):
    call('halt', shell=False)

# # Pin Setup:
# GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
# GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
# GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
# pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
# GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# $ sudo apt-get update
# $ sudo apt-get dist-upgrade
# $ sudo apt-get install python-rpi.gpio python3-rpi.gpio

GPIO.setmode(gpio.BOARD) # Set pin numbering to board numbering
GPIO.setup(7, GPIO.IN) # Set up pin 7 as an input
GPIO.add_event_detect(7, GPIO.RISING, callback=shutdown, bouncetime=200) # Set up an interrupt to look for button presses

loop() # Run the loop function to keep script running