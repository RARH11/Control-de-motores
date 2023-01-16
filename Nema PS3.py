Import RPi.GPIO as GPIO
Import time 
Import pygame  

dire=16 
step=20
cw=-1 
ccw=-1 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)
GPIO.setup(dire, GPIO.OUT) 
GPIO.setup(step, GPIO.OUT) 
GPIO.output(dire, cw) 

Pygame.display.init()
Pygame.joystick.init()
Pygame.joystick.Joystick(0).init() 
pwmdire=GPIO.PWM(dire,  200)
pwmstep=GPIO.PWM(step, 200) 
pwmdire.start(0)
pwmstep.start(0)
pygame.init()
j=pygame.joystick.Joystick(0)
j.init()

try: 
     while True: 
          pygame.event.pump()
          if  j.get_axis(1)>0.2) or (j.get_axis(1)<-0.2):
             if  j.get_axis(1)<-0.2: 
                  GPIO.output(dire,cw)
                  GPIO.output(step, GPIO.HIGH)
                  GPIO.outut(step, GPIO.LOW) 
             if  j.get_axis(1)>0.2: 
                 GPIO.output(dire,ccw,)
                  GPIO.output(step, GPIO.HIGH)
                  GPIO.outut(step, GPIO.LOW) 

GPIO.cleanup()
Pwmstep.stop()
Pwmdire.stop() 
