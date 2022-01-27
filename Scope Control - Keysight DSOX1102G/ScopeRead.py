# ScopeRead.py
# Written by Srikanth Sugavanam, IIT Mandi, India - 26th January 2022

# This module is written as a wrapper for the Pymeasure library for controlling the
# Keysight DSOX1102G oscilloscope. This is a code in development, and will be updated
# from time to time. Please refer to the original pymeasure readthedocs page for more
# information

import pymeasure
import pyvisa as visa
from pymeasure.instruments.keysight import KeysightDSOX1102G as Kscope
import matplotlib.pyplot as plt
import numpy as np


def initialize():
    rm = visa.ResourceManager('@py')
    instr = (rm.list_resources())
    print(instr)
    
    pymscope = Kscope.KeysightDSOX1102G(instr[1])
    print('Scope initialized...')
    return pymscope

def triggerset_ch2(pymscope,triglevel,channel):
    pymscope.write(':TRIG:SWE NORM')
    stringout = ':TRIG:MODE EDGE'
    pymscope.write(stringout)
    stringout = ':TRIG:LEV '+str(triglevel)
    pymscope.write(stringout)
    stringout = ':TRIG:SOUR CHAN'+str(channel)
    pymscope.write(stringout)
    print('Trigger set...')

def acquire_ch2(pymscope):
    ch2, ch2_preamble = pymscope.download_data(source = "channel2")
    t = np.arange(0,ch2_preamble['points'],1)*ch2_preamble['xincrement'] #arange format - start, end, step
    
    print('Data acquired...')
    return t, ch2

def store(fname,t,ch2):
    fname_t = fname+'_t.csv'
    fname_ch2 = fname+'_ch2.csv'
    
    np.savetxt(fname_t,t,delimiter = ',')
    np.savetxt(fname_ch2,ch2,delimiter = ',')
    
    print('Data saved as %s and %s.' %(fname_t, fname_ch2))

# fname_t = '/home/pi/Documents/Python_programmes/IC231/Pot_run1_t.csv'
# fname_ch2 = '/home/pi/Documents/Python_programmes/IC231/Pot_run1_ch2.csv'
# 
# np.savetxt(fname_t,t,delimiter = ',')
# np.savetxt(fname_ch2,ch2,delimiter = ',')
# 
# plt.plot(t,ch2);
# plt.show()
