import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN )
GPIO.setup(24, GPIO.OUT, initial=1 )
GPIO.output(24, True)
n=0
while True:
#if n == 1 :
    i = GPIO.input(25)
    print(i)
    GPIO.output(24,0)
    print("low")
    sleep(1)
    GPIO.output(24,1)
    print("high")
    sleep(1)
    