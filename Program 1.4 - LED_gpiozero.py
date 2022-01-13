from gpiozero import LED,Button
from signal import pause

orange = LED(17)
button = Button(27)

# while True:
#     orange.on()
#     sleep(0.1)
#     orange.off()
#     sleep(0.1)
    
button.when_pressed = orange.on
button.when_released = orange.off

