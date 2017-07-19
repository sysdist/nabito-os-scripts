import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
#//BY CHOW
from pyA20.gpio import connector

#led = connector.LEDp1    # This is the same as port.POWER_LED
led = port.PA1 #connector.LEDp2    # This is the same as port.STATUS_LED
#led = port.POWER_LED
#led = port.STATUS_LED

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)
gpio.output(led, 1)
print ("Goodbye.")

