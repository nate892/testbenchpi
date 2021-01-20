
import RPi.GPIO as GPIO
from time import sleep

##GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN )
GPIO.setup(27, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    

while True:
    i = GPIO.input(4)
    u = GPIO.input(17)
    k = GPIO.input(27)
    y = GPIO.input(22)
    sleep(.5)
    print(i,u,k,y)