from machine import Pin
from time import sleep

display_1 = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT)
]

display_0 = [
    Pin(7, Pin.OUT),
    Pin(8, Pin.OUT),
    Pin(9, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT)
]

for each in range(7):
    display_0[each].toggle()
    display_1[each].toggle()

contador_0 = 0
contador_1 = 0

while contador_0 < 10:
    while contador_1 < 10:
        if contador_1 == 0:
            display_1[0].off()
            display_1[1].off()
            display_1[2].off()
            display_1[3].off()
            display_1[4].off()
            display_1[5].off()
            display_1[6].on()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 1:
            display_1[0].on()
            display_1[1].off()
            display_1[2].off()
            display_1[3].on()
            display_1[4].on()
            display_1[5].on()
            display_1[6].on()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 2:
            display_1[0].off()
            display_1[1].off()
            display_1[2].on()
            display_1[3].off()
            display_1[4].off()
            display_1[5].on()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 3:
            display_1[0].off()
            display_1[1].off()
            display_1[2].off()
            display_1[3].off()
            display_1[4].on()
            display_1[5].on()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 4:
            display_1[0].on()
            display_1[1].off()
            display_1[2].off()
            display_1[3].on()
            display_1[4].on()
            display_1[5].off()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 5:
            display_1[0].off()
            display_1[1].on()
            display_1[2].off()
            display_1[3].off()
            display_1[4].on()
            display_1[5].off()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 6:
            display_1[0].off()
            display_1[1].on()
            display_1[2].off()
            display_1[3].off()
            display_1[4].off()
            display_1[5].off()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 7:
            display_1[0].off()
            display_1[1].off()
            display_1[2].off()
            display_1[3].on()
            display_1[4].on()
            display_1[5].on()
            display_1[6].on()
            contador_1 += 1
            sleep(1)
        elif contador_1 == 8:
            display_1[0].off()
            display_1[1].off()
            display_1[2].off()
            display_1[3].off()
            display_1[4].off()
            display_1[5].off()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
        else: 
            display_1[0].off()
            display_1[1].off()
            display_1[2].off()
            display_1[3].off()
            display_1[4].on()
            display_1[5].off()
            display_1[6].off()
            contador_1 += 1
            sleep(1)
            contador_0 += 1
    if contador_0 == 0:
        display_0[0].off()
        display_0[1].off()
        display_0[2].off()
        display_0[3].off()
        display_0[4].off()
        display_0[5].off()
        display_0[6].on()
        contador_1 = 0
    elif contador_0 == 1:
        display_0[0].on()
        display_0[1].off()
        display_0[2].off()
        display_0[3].on()
        display_0[4].on()
        display_0[5].on()
        display_0[6].on()
        contador_1 = 0
    elif contador_0 == 2:
        display_0[0].off()
        display_0[1].off()
        display_0[2].on()
        display_0[3].off()
        display_0[4].off()
        display_0[5].on()
        display_0[6].off()
        contador_1 = 0
    elif contador_0 == 3:
        display_0[0].off()
        display_0[1].off()
        display_0[2].off()
        display_0[3].off()
        display_0[4].on()
        display_0[5].on()
        display_0[6].off()
        contador_1 = 0
    elif contador_0 == 4:
        display_0[0].on()
        display_0[1].off()
        display_0[2].off()
        display_0[3].on()
        display_0[4].on()
        display_0[5].off()
        display_0[6].off()
        contador_1 = 0
    elif contador_0 == 5:
        display_0[0].off()
        display_0[1].on()
        display_0[2].off()
        display_0[3].off()
        display_0[4].on()
        display_0[5].off()
        display_0[6].off()
        contador_1 = 0
    elif contador_0 == 6:
        display_0[0].off()
        display_0[1].on()
        display_0[2].off()
        display_0[3].off()
        display_0[4].off()
        display_0[5].off()
        display_0[6].off()
        contador_1 = 0
    elif contador_0 == 7:
        display_0[0].off()
        display_0[1].off()
        display_0[2].off()
        display_0[3].on()
        display_0[4].on()
        display_0[5].on()
        display_0[6].on()
        contador_1 = 0
    elif contador_0 == 8:
        display_0[0].off()
        display_0[1].off()
        display_0[2].off()
        display_0[3].off()
        display_0[4].off()
        display_0[5].off()
        display_0[6].off()
        contador_1 = 0
    else: 
        display_0[0].off()
        display_0[1].off()
        display_0[2].off()
        display_0[3].off()
        display_0[4].on()
        display_0[5].off()
        display_0[6].off()
        contador_1 = 0
        contador_0 = -1 