import RPi.GPIO as GPIO   
from time import sleep 
import pygame 

servo=20

GPIO.setmode(GPIO.BCM)   #pines en formato BCM
GPIO.setwarnings(False)

pygame.display.init()
pygame.joystick.init()
pygame.joystick.joystick(0).init()
GPIO.setup(servo, GPIO.OUT)
pwmservo= GPIO.PWM(servo,40)  #pulso PWM en 40
pwmservo.start(0)
pygame.init()
j=pygame.joystick.joystick(0) #nombrar el mando PS3 para abreviar mas adelante
j.init()

try:
  while True:
    pygame.event.pump()
    if j.get_button(16):   #boton de direccion derecho 
      for x in range (0,6):
        pwmservo.ChangeDutyCycle(x)
        sleep(0.2)
    if j.get_button(15):  #boton de direccion izquierdo 
      for x in range (6,1, -1):
        pwmservo.ChangeDutyCycle(x)
        sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()
  pwmservo.stop()
