#Distance measurement using HC-SR04 using software triggered pulses.

#Tasks:
#Analyse the effect of time sleep in line 30
#Analayse the correlation of trigger signal and the echo signal
#Extend the code to measure the repeatability of the measurement
#Improve the repeatability by averaging. What is the effect on time resolution. 

import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
TRIG = 13
ECHO = 18 
 
#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# set Trigger to FALSE for sensor settlement
GPIO.output(TRIG, False)
time.sleep(0.5)

try:
    while True:


        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
 
        # save StartTime
        while GPIO.input(ECHO) == 0:
            StartTime = time.time()
 
            # save time of arrival
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()
 
        TimeElapsed = (StopTime - StartTime)*1E6
        print('The sound travelled %d μs' %TimeElapsed)
        
        time.sleep(0.1)
      
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Measurement stopped by User")
    