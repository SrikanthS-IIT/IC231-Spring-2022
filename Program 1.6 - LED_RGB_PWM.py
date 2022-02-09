import RPi.GPIO as GPIO
import time
#import threading as th


#Defines the RGB pins
LED_PIN_R = 13
LED_PIN_G = 27
LED_PIN_B = 22

#Enables to label using GPIO numbers instead of pin numbers
GPIO.setmode(GPIO.BCM)

#Define the controlled pin as output
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)
GPIO.setup(LED_PIN_B, GPIO.OUT)

#defines the frequency of one PWM cycle
freq = 1000000

#Define 8bit RGB level of individual colors
R = 125
G = 255
B = 255

#Scaling of duty cycle to a number between 0 and 100
dutycycle_R = 100*R/255
dutycycle_G = 100*G/255
dutycycle_B = 100*B/255

#Initiate red LED
soft_pwm_R = GPIO.PWM(LED_PIN_R,freq)
soft_pwm_R.start(dutycycle_R)

#Initiate green LED
soft_pwm_G = GPIO.PWM(LED_PIN_G,freq)
soft_pwm_G.start(dutycycle_G) 

#Initiate blue LED
soft_pwm_B = GPIO.PWM(LED_PIN_B,freq)
soft_pwm_B.start(dutycycle_B)

#Wait for keyboard input to stop programm
input('Press any key to exit the program!')


soft_pwm_R.stop()
soft_pwm_G.stop()
soft_pwm_B.stop()

#Shutdown all ports 
GPIO.cleanup()


