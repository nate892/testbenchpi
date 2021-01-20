from mcp3208 import MCP3208
import time 

adc = MCP3208()

data=[0,0,0,0,0,0,0,0]

while True:
   bits = adc.read(0)
   volts = bits#((5 * bits )/ 4096)
   print(volts)
   time.sleep(0.25)
    