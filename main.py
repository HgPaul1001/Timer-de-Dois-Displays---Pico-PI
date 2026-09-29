from machine import Pin
from time import sleep

display_u = [0,0,0,0,0,0,0]
display_d = [0,0,0,0,0,0,0]
for each in range(7):
    display_u[each] = Pin(each, Pin.OUT)
    display_d[each] = Pin(each+7, Pin.OUT)



digito = [
[0, 0, 0, 0, 0, 0, 1], #zero
[1, 0, 0, 1, 1, 1, 1], #um
[0, 0, 1, 0, 0, 1, 0], #dois
[0, 0, 0, 0, 1, 1, 0], #tres
[1, 0, 0, 1, 1, 0, 0], #quatro
[0, 1, 0, 0, 1, 0, 0], #cinco
[0, 1, 0, 0, 0, 0, 0], #seis
[0, 0, 0, 1, 1, 1, 1], #sete
[0, 0, 0, 0, 0, 0, 0], #oito
[0, 0, 0, 0, 1, 0, 0]  #nove
]
#Desligar os LEDs
for each in range(7):
    display_d[each].value(digito[0][each])
    display_u[each].value(digito[0][each])

while True:
    for d in range(10):
        for each in range(7):
            display_d[each].value(digito[d][each])
        print("dezena")      
        for u in range(10):
            for each in range(7):
                display_u[each].value(digito[u][each])
            sleep(1)
            print("unidade")        