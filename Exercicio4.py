##Titulo do Programa: LDR
##Author: Marcelo Soares Barroso
##Data: 01/07/2018
##Objetivo: em função do estado da iluminação da sala, acenda um Led amarelo caso esteja baixa, ou um led vermelho para o caso de uma iluminação forte. Utilize um LDR para medição da intensidade luminosa do ambiente.


import machine 
import utime


pin21 = machine.Pin(21, machine.Pin.OUT)
pin22 = machine.Pin(21, machine.Pin.OUT)
pin34 = machine.Pin(34, machine.Pin.IN)
adc = machine.ADC(machine.Pin(34))

while True:
  if (adc.read() > 2000):    
      pin21.value(1)  
  else:
  pin22.value(1)
  print(pin34.value())
  print(adc.read())  
  utime.sleep_ms(100)