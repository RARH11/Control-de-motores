Import RPi.GPIO as GPIO  #libreria RPi.GPIO
Import time              #libreira time    
Import pygame            #libreria pygame, permite vincular el control de PS3

dire=16                  #habilitar pin 16 
step=20                  #habilitar pin 20
cw=-1                    #Variable cw
ccw=-1                   #Variable ccw

GPIO.setmode(GPIO.BCM)  #habilitar pines en formato BCM
GPIO.setwarnings(false)
GPIO.setup(dire, GPIO.OUT) #habilitar pin en salidad
GPIO.setup(step, GPIO.OUT) #habiliotar pin en salidad 
GPIO.output(dire, cw) 

Pygame.display.init()   #Inicializa el atributo display del mando PS3
Pygame.joystick.init()  #Inicializa el atributo Joystick del mando PS3
Pygame.joystick.Joystick(0).init() 
pwmdire=GPIO.PWM(dire,  200)    
pwmstep=GPIO.PWM(step, 200) 
pwmdire.start(0)      #inicio del motor
pwmstep.start(0)
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
                  GPIO.output(step, GPIO.HIGH)
                  GPIO.outut(step, GPIO.LOW) 
             if  j.get_axis(1)>0.2: 
                 GPIO.output(dire,ccw,)   #giro al sentido contrario del reloj 
                  GPIO.output(step, GPIO.HIGH)
                  GPIO.outut(step, GPIO.LOW) 

GPIO.cleanup()               #Finaliza los pines 
Pwmstep.stop()
Pwmdire.stop() 
