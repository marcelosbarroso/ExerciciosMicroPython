##Titulo do Programa: Acendimento por PWM.
##Author: Marcelo Soares Barroso
##Data: 01/07/2018
##Objetivo: fazer um led piscar em regime de fading, isto é, com acendimento e apagamento gradual. Utilizar para esta finalidade a função PWM.

import time
import machine
pwm = machine.PWM(machine.Pin(23))
pwm.freq(100)
while True:
    for i in range(1024):
        pwm.duty(i)
        time.sleep(0.001)
    for i in range(1023, -1, -1):
        pwm.duty(i)
        time.sleep(0.001)