import pigpio
import time
#Before running this programm: Enable pigpiod daemeon bey executing command "sudo pigpiod"
#Hardware PWM enables accuracy to a microsecond
pi = pigpio.pi()

frequency = 100000
dutycycpercent = 50#1E-6
dutycyc = int(dutycycpercent/100*1E6)

#Hardware pins are initiaited through Broadcom number
pi.hardware_PWM(18, frequency,dutycyc )

#Wait for keyboard input to stop programm
print('Press any key to exit the program')
input()
pi.hardware_PWM(18, 0, 0)



