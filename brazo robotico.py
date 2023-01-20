Import RPi.GPIO as GPIO  #libreria RPi.GPIO
from time import sleep   #libreira time    
Import pygame            #libreria pygame, permite vincular el control de PS3

servo4=25                #habilitar pin 25
servo3=24                #habilitar pin 24
servo2=23                #habilitar pin 23
servo=22                 #habilitar pin 22
dire=20                  #habilitar pin 20 
step=16                  #habilitar pin 16
direc=17                 #habilitar pin 17
ste=27                   #habilitar pin 27
cw=1                    #Variable cw
ccw=0                   #Variable ccw
ew=1                    #Variable ew
cew=0                   #Variable cew

GPIO.setmode(GPIO.BCM)  #habilitar pines en formato BCM
GPIO.setwarnings(false)
GPIO.setup(dire, GPIO.OUT) #habilitar pin en salida
GPIO.setup(step, GPIO.OUT) #habilitar pin en salida 
GPIO.setup(direc, GPIO.OUT) #habilitar pin en salida
GPIO.setup(ste, GPIO.OUT) #habilitar pin en salida 
GPIO.output(dire, cw) 
GPIO.output(direc, ew)
GPIO.setup(servo, GPIO.OUT) #habilitar pin en salida
pwmservo= GPIO.PWM(servo,40) #Frecuencia  
pwmservo.start(0) #Inicio del servomotor
GPIO.setup(servo2, GPIO.OUT) #habilitar pin en salida
pwmservo2= GPIO.PWM(servo2,40) #Frecuencia  
pwmservo2.start(0) #Inicio del servomotor
GPIO.setup(servo3, GPIO.OUT) #habilitar pin en salida
pwmservo3= GPIO.PWM(servo3,40) #Frecuencia  
pwmservo3.start(0) #Inicio del servomotor
GPIO.setup(servo4, GPIO.OUT) #habilitar pin en salida
pwmservo4= GPIO.PWM(servo4,40) #Frecuencia  
pwmservo4.start(0) #Inicio del servomotor

Pygame.display.init()   #Inicializa el atributo display del mando PS3
Pygame.joystick.init()  #Inicializa el atributo Joystick del mando PS3
Pygame.joystick.Joystick(0).init() 
pygame.init()         #inicio del mando PS3 
j=pygame.joystick.Joystick(0)  #valores del mando de PS3 en 0
j.init()

try: 
     while True: 
          pygame.event.pump()
          if  j.get_axis(1)>0.2) or (j.get_axis(1)<-0.2):     #Condicion del joystick 1 para activar 
                                                   #solo cuando esta a mas del 20 por ciento de su valores 
             if  j.get_axis(1)<-0.2: 
                  GPIO.output(dire,cw)     #giro al sentido del reloj 
                  for x in range(2):       #avance de 2 pasos(2 grados)
                    GPIO.output(step, True)
                    sleep(0.01)
                    GPIO.outut(step, False)
                    sleep(0.01)
                  GPIO.output(direc, ew)   #giro al sentido del reloj del segundo motor
                  for xin range(2):        #avance de 2 pasos(2 grados)
                    GPIO.output(ste, True)
                    sleep(0.01)
                    GPIO.outut(ste, False)
                    sleep(0.01)
             if  j.get_axis(1)>0.2: 
                 GPIO.output(dire,cw)     #giro al sentido contrario del reloj 
                  for x in range(2):       #avance de 2 pasos(2 grados)
                    GPIO.output(step, True)
                    sleep(0.01)
                    GPIO.outut(step, False)
                    sleep(0.01)
                  GPIO.output(direc, ew)   #giro al sentido contrario del reloj del segundo motor
                  for xin range(2):        #avance de 2 pasos(2 grados)
                    GPIO.output(ste, True)
                    sleep(0.01)
                    GPIO.outut(ste, False)
                    sleep(0.01)
                    
          if j.get_button(7): 
            for y in range(0,6):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(6): 
            for y in range(5,0, -1):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(4): 
            for y in range(0,6):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(5): 
            for y in range(5,0, -1):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(15): 
            for y in range(0,6):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(16): 
            for y in range(5,0, -1):
              pwmservo.ChangeDutyCycle(y)
              sleep(4)
          if j.get_button(1): 
            for y in range(0,3):
              pwmservo.ChangeDutyCycle(y)
              sleep(0.1)
          if j.get_button(3): 
            for y in range(5,1, -1):
              pwmservo.ChangeDutyCycle(y)
              sleep(0.1)
              
except KeyboardInterrpt:
  GPIO.cleanup()
  pwmstep.stop()
  pwmdire.stop()
  pwmste.stop()
  pwmdirec.stop()
  pwmservo.stop()
  pwmservo2.stop()
  pwmservo3.stop()
  pwmservo4.stop()
