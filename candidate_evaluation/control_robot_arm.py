import time
from glob import glob

import random
import requests
from pydobot import Dobot


def connect_dobot():

    available_ports = glob('/dev/ttyUSB0')  # mask for OSX Dobot port

    if len(available_ports) == 0:
        print("NOT FOUND!!!")
        print('no port found for Dobot Magician')
        exit(1)
    #
    device = Dobot(port=available_ports[0])
    print("Connected")

    return device



device = connect_dobot()

ink_x = 0.0
ink_y = -200.0 + random.randint(-20,20)

passport_z = -35.0
ink_z = -27.0

positive_thumb = -90.0
negative_thumb = 90.0


device.speed(100)

# device.go(0.0, 170.0, 25.0, 0.0) # Start
device.go(0.0, 180.0, 25.0, 0.0) # Start
# device.go(0.0, 170.0, 25.0,180) # Start
time.sleep(0.5)

#
#
# device.go(ink_x+50, 50, 25.0) # Start
# time.sleep(1.0)

device.go(ink_x, ink_y, 80) # stempel
time.sleep(0.5)
device.speed(10)
device.go(ink_x, ink_y, -20.0,0) # stempel ned
time.sleep(0.5)
device.speed(100)
device.go(ink_x, ink_y, ink_z,90) # stempel ned
device.go(ink_x, ink_y, ink_z,40) # stempel ned
time.sleep(1.5)
device.go(ink_x, ink_y, 80.0) # stempel ned
time.sleep(1.0)
#
#
#
#
#
#
#
device.go(200.0, 0.0, 20,positive_thumb) # stempel
device.speed(10)
device.go(200.0, 0.0, 0.0,positive_thumb) # stempel ned
time.sleep(0.5)
if(True):
    device.speed(100)
    device.go(200.0, 0.0, 0,positive_thumb) # stempel ned
    time.sleep(0.5)
    device.go(200.0, 0.0, passport_z,positive_thumb) # stempel ned
    time.sleep(1.5)
    device.go(200.0,0.0,0,positive_thumb)  # stempel ned
    time.sleep(0.5)
else:
    device.speed(100)
    device.go(200.0, 0.0, 0,negative_thumb) # stempel ned
    time.sleep(0.5)
    device.go(200.0, 0.0, passport_z,negative_thumb) # stempel ned
    time.sleep(1.5)
    device.go(200.0,0.0,0,negative_thumb)  # stempel ned
    time.sleep(0.5)


# device.go(200.0, 0.0, 0.0) # stempel ned


device.go(200.0, 0.0, 20.0) # stempel ned



device.speed(100)

device.go(0.0, 180.0, 10.0) # Start
time.sleep(1.5)
device.go(0.0, 60.0, 35.0) # Start
device.close()