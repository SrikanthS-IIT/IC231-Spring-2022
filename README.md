# IC231-Spring-2022
Codes and materials related to my IC231 Measurement and Instrumentation course offered in Spring 2022 at IIT Mandi.

#Raspberry Pi based Measurement and Instrumentation Labs
##Srikanth Sugavanam, Erwin Fuhrer, School of Computing and Electrical Engineering, IIT Mandi.
###First write - 18th January 2022


Abstract

The following is a document that provides information and links to resources on how to get your Raspberry Pi up and running for remote access lab sessions. The instructions provided here will allow you to set up the necessary files and Python libraries for access of the GPIO pins, and facilitating remote access of USB-based  devices. 

IMPORTANT - See the C for CAUTION section before you start. 


Start.

Equipment and packages used
	1. Raspberry Pi 4B+
	2. Raspbian OS version - Raspbian GNU/Linux 11 (Bullseye) 
	3. Python version - 3.9.2
	4. PyVisa version - 1.11.3
	5. Thonny IDE
	6. Pymeasure v0.9
	7. Pandas v1.3 (v1.4 available since January 22, 2022)
	8. Balena Etcher for burning the OS image
	9. PyUSB, PySerial (usually installed with PyVisa)
	10. gpiozero library
	11. RPi.GPIO library
	12. raspi-blinka - CircuitPython libraries for interfacing with ADS111s
	13. adafruit_bus_device
	14. adafruit_circuitpython_ads1x15
	15. VNC Server (pre-installed on RPi)
	16. VNC Viewer (on your remote computer)
	
A. Prepping the Raspi
=====================
Burn the Raspberry Pi OS image onto an SD disk using the Balena Etcher software. Once this is done, follow the usual approach for setting up your Raspberry Pi. Enable SPI, I2C, VNC using the raspi-config command in the terminal, or via the RPi button>Preferences>Raspberry Pi Configuration option. 

Python and Thonny come pre-installed, so this is not required. 

B. Installing the Python libraries
==================================
There is a sequence to installing some of the libraries owing to the dependencies. Normally, these install automatically, however I ran into a bug when installing pymeasure. So the recommended sequence is as follows.

1. gpiozero
2. RPi.GPIO
3. PyUSB, PySerial
4. PyVisa
5. Pandas
6. Pymeasure (ONLY AFTER PANDAS)
7. adafruit-blinka 
8. adafruit_circuitypython_busdevice (AFTER raspi-blinka)
9. adafruit_circuitpython_ads1x15 (AFTER raspi-blinka)

The usual terminal commands usually work for installation of the libraries above. For me the pandas and rasp-blinka install were glitchy. The following worked for me - 

	pip3 install adafruit-blinka
	sudo apt-get install python3-pandas

NOTE - I used the pymeasures library as it has pre-written routines for communicating with the Keysight DSOX1102G. If you run into errors where it says something along the lines of '... no such file exists...' it is most likely because of a uppercase/lowercase error in the library definition. You can either do a git pull, or as a quick fix (not recommended, but works) - physically go in and change the case of the character. Be careful not to change any other code! :)

C for CAUTION - Python 2 vs. Python 3, Raspberry 32 bit vs. 64 bit
===================================================================

The Adafruit libraries are used here for working with the ADS1115s. However, there is a catch - the Blinka library support is only limited to Python3 currently. Furthermore, CircuitPython supports only the 32 bit version of the Raspberry Pi OS. See here for more information - https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi 

Use the terminal command <uname -m> - if the output is armv7l, then your OS is 32 bit and you will be able to use the CircuitPython and Blinka libraries. 

D. Instrument connection resources
==================================+

For our labs we use the Keysight DSOX1102G oscilloscope, and operated remotely using the Pymeasure library (https://pymeasure.readthedocs.io/en/latest/). The oscilloscope is controlled remotely via USB. 

In principle, if you install the above mentioned libraries in sequence, you should have no problem in communicating remotely with the peripherals (see for example this website - https://hackaday.com/2016/11/16/how-to-control-your-instruments-from-a-computer-its-easier-than-you-think/. Also see Keithley's application note on using Raspberry Pi 3 models in the lab - https://download.tek.com/document/1KW-61463-0__Raspberry_Pi_3_Save_Lab_Space_%20Cost_Application_Note_090718.pdf 

To check the list of remote devices connected to your Raspberry Pi, you can use a simple code of the following form - 

	import pyvisa as visa

	rm = visa.ResourceManager('@py')
	instr = (rm.list_resources())
	print(instr)
	
This simple code should print out the list of devices connected. 

D.1 - USB device control with pyvisa
====================================

Now, it may so happen that Raspberry Pi is unable to connect to USB devices. This apparently arises as there is 'an inherent rule in VISA about USB devices being set to “read only”, limiting their access...' - as identified by the authors of the original Keithley application note, and subsequently addressed in the following LinkedIn post - https://www.linkedin.com/pulse/revisiting-keithleys-app-note-featuring-raspberry-pi-its-joshua-brown/ 

Essentially, to enable USB device identification, you will have to edit one of the rule files of the Raspberry Pi - OS as detailed in the above post (sounds scary, but it worked). After a reboot, if you run the same pyvisa code snippet, the USB device should then appear on the list. 






