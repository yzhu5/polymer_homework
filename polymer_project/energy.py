import numpy as np
import math
import matplotlib.pyplot as plt


#u = np.arange(0.001,0.5,0.001)
kb = 1.38*10**(-23)
t = 300
q = 10

u = np.arange(0.01,0.5,0.01)
b = np.arange(0,25,1)
a = np.arange(0.01,3.14,0.1)
c = np.arange(0.01,6.28,0.1)

all_u = []
all_f = []
all_ftm =[]

for ui in u[:]:
	
	fi = ui/q*t*kb*(math.log(ui*0.1)+math.log(0.07961783)+q*ui)

	

	all_u.append((ui))
	all_f.append((fi))


plt.figure()
plt.plot(all_u,all_f)

plt.show()