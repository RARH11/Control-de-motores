from time import sleep    #libreria time y habilitar sleep 
import RPi. GPIO as GPIO  
GPIO.setmode(GPIO.BCN)   #pines en formato BCN
servo=20                #pin 20 habilitado 
GPIO.setup(servo, GPIO.OUT)   #pin en modo salidad 
pwm =GPIO.PWM(servo, 50)   #pulso o frecuencia (este sera el valor a modificar) 
pwm.start(0)

try: 
      while True: 
           for X in range (0, 7) :   #rango del servo
                 pmw.ChangeDutyCycle(x) 
                 sleep(0.1)
           for X in range(7, 0, -1): 
                 pwm.ChangeDutyCycle(x)
                 sleep(0.1) 
      #El rango del servo seria 0 igua a 0 grados y 15 igual a 270 grados 
except  KeyboardInterrupt:
GPIO.cleannup()  
