import RPi.GPIO as gpio
import time

#Define the pin we want to control
LED_PIN = 17
#Enables to label using GPIO numbers instead of pin numbers
gpio.setmode(gpio.BCM)
#Define the controlled pin as output
gpio.setup(LED_PIN, gpio.OUT)

#defines the frequency of one PWM cycle
#Change the frequency logarithmically from 1 Hz to 10 kHz 
freq = 10

try:
    while True:
    
        gpio.output(LED_PIN, gpio.HIGH)
        time.sleep((1/freq)/2)
        gpio.output(LED_PIN, gpio.LOW)
        time.sleep((1/freq)/2)

except KeyboardInterrupt:
    print('Exit program')

finally:
    gpio.output(17,gpio.LOW)
    gpio.cleanup()






