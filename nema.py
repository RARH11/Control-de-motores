from time import sleep
import RPi.GPIO as gpio

DIR=20 #CW+
STEP=21 #CLK+
CW=1
CCW=0

gpio.setmode(gpio.BCM)     #Configuracion de los pines en formato BCM
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR, CW)

try:
  while True:
    sleep(1)
    gpio.output(DIR, CW)    #Giro al sentido del reloj 
    for x in range (400):   #Numero de pasos que avanzara el motor
      gpio.output(STEP, gpio.HIGH)
      sleep(0.01)
      gpio.output(STEP, gpio.LOW)
      sleep(0.01)
      
    sleep(1)
    gpio.output(DIR, CCW)   #Giro al sentido contrario del reloj 
    for x in range (400):   #Numero de pasos que avanzara el motor 
      gpio.output(STEP, gpio.HIGH)
      sleep(0.01)
      gpio.output(STEP, gpio.LOW)
      sleep(0.01)


except KeyboardInterrupt:  #permite fializar el uso de los pines 
  gpio.cleanup()
