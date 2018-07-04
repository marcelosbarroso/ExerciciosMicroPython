##Titulo do Programa: Cliente we com led
##Author: Marcelo Soares Barroso
##Data: 01/07/2018
##Objetivo: Faça um cliente web que leia um número de um site e acenda o correspondente número de leds. Variar o número no site de 1 a 4.


from microWebCli import MicroWebCli
import network
import machine

pin23 = machine.Pin(23, machine.Pin.OUT)
pin22 = machine.Pin(22, machine.Pin.OUT)
pin21 = machine.Pin(21, machine.Pin.OUT)
pin19 = machine.Pin(19, machine.Pin.OUT)
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("marcelo", "19830000")
station.isconnected()
station.ifconfig()

pin23.value(0)
pin22.value(0)
pin21.value(0)
pin21.value(0)

leitura_site = MicroWebCli.GETRequest('http://olaria.ucpel.edu.br/soiiesp/n1.php')
total_leds=int(leitura_site)
print(total_leds)
if total_leds == 1:
   pin23.value(1)
if total_leds == 2:
   pin23.value(1)
   pin22.value(1)
if total_leds == 3:
   pin23.value(1)
   pin22.value(1)
   pin21.value(1)
if total_leds == 4:
   pin23.value(1)
   pin22.value(1)
   pin21.value(1)
   pin19.value(1)