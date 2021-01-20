import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
while True:
    GPIO.output(26, True)
    sleep(1)
    GPIO.output(26, False)
    sleep(1)
    
    GPIO.output(19, True)
    sleep(1)
    GPIO.output(19, False)
    sleep(1)
    
    GPIO.output(13, True)
    sleep(1)
    GPIO.output(13, False)
    sleep(1)
    
    GPIO.output(6, True)
    sleep(1)
    GPIO.output(6, False)
    sleep(1)
    
    GPIO.output(5, True)
    sleep(1)
    GPIO.output(5, False)
    sleep(5)
    
    

