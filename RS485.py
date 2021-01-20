import serial
ser =  serial.Serial('/dev/ttyS0', 9600, timeout=1)
s = ser.readlines(200)
print(s)

