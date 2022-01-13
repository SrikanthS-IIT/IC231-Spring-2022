import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)
 
channel = 17
gpio.setup(channel, gpio.OUT)
gpio.output(channel,gpio.LOW)


while True:
    gpio.output(channel,gpio.HIGH)
    
gpio.output(channel,gpio.LOW)
gpio.cleanup()

