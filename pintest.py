import time
import RPi.GPIO as GPIO

powerfail_pin = 25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(powerfail_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def safe_shut_down():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print (output)

i=0
print(i)

while True:
    pin_status = GPIO.input(powerfail_pin)
    print(pin_status)
    time.sleep(1)


        
