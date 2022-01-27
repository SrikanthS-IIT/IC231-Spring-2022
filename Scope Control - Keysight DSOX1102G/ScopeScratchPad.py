import X9C103_BCM as pot
import ScopeRead as scope
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

scope_id = scope.initialize()

scope.triggerset_ch2(scope_id,1.5,2)
scope_id.single()

CS = 16
INC = 20
UD = 21
#GND = pin34
delay = 0.1
# 
pot.initiate(CS,INC,UD)
pot.activate(CS,INC,UD)

pot.reset(CS,INC,UD)

pot.disconnect(CS,INC,UD)
sleep(5)   #To give some time to the scope to display the acquired data. Otherwise you will run into timeout.
# 
data = scope.acquire_ch2(scope_id)

t = data[0]
ch2 = data[1]

scope.store('Pot_run3',t,ch2)

plt.plot(t,ch2);
plt.show()