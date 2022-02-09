#Before running this programm: Enable pigpiod daemeon bey executing command "sudo pigpiod"
#Hardware PWM enables accuracy to a microsecond
import pigpio
pi = pigpio.pi()

#set Pin (pigpio uses BCM labeling)
pin = 13

#Define PWM wave parameters
frequency = 100
dutycycpercent = 50#1E-6
dutycyc = int(dutycycpercent/100*1E6)

#Hardware pins are initiaited through Broadcom number
pi.hardware_PWM(pin, frequency,dutycyc )

#Wait for keyboard input to stop programm
print('Press any key to exit the program')
input()
pi.hardware_PWM(pin, 0, 0)




