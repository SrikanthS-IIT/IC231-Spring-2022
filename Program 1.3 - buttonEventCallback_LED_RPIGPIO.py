import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

gpio.setup(27,gpio.IN)
gpio.setup(17,gpio.OUT)

# gpio.cleanup(27)
# gpio.cleanup(17)


gpio.add_event_detect(27,gpio.FALLING)
# gpio.setup(27, gpio.IN, pull_up_down = gpio.PUD_UP)  #Use this code if hardware pull-down
                                                       #is not implemented 

try:
    while True:
        if gpio.event_detected(27):
            print("closed")
            gpio.output(17,gpio.HIGH)
            sleep(0.1)
            gpio.output(17,gpio.LOW)
            sleep(0.1)
            gpio.output(17,gpio.HIGH)
            sleep(0.1)
            gpio.output(17,gpio.LOW)
            sleep(0.1)
            gpio.output(17,gpio.HIGH)
            sleep(0.1)
            gpio.output(17,gpio.LOW)
            sleep(0.1)
                
            
finally:
 
    gpio.cleanup(17)
    gpio.cleanup(27)
