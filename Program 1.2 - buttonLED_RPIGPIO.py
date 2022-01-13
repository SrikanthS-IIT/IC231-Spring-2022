import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(27,gpio.IN)
gpio.setup(17,gpio.OUT)

# gpio.setup(27, gpio.IN, pull_up_down = gpio.PUD_UP)

try:
    while True:
        if gpio.input(27)==0:
            print("open")
            gpio.output(17,gpio.LOW)
        else:
            print("closed")
            gpio.output(17,gpio.HIGH)
            
finally:
    gpio.output(17,gpio.LOW)
    gpio.cleanup()