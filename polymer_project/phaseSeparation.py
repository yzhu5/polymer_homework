import numpy as np
import math
import matplotlib.pyplot as plt


#u = np.arange(0.001,0.5,0.001)
kb = 1.38*10**(-23)
t = 300
q = 10

u = np.arange(0.01,0.5,0.1)
b = np.arange(0,25,1)
a = np.arange(0.01,3.14,0.1)
c = np.arange(0.01,6.28,0.1)

all_u = []
all_f = []
all_ftm =[]

for ui in u[:]:
	
	fi = ui/q*t*kb*(math.log(ui*0.1)+math.log(0.07961783)+q*ui)
	a0 = 0
	#A1 = 0
	#print(fi)
	all_u.append((ui))
	all_f.append((fi))

	ftm = 999
	for bi in b[:]:
		print(bi)
		#a0 = 0
		for ai in a[:]:
			
			a0 =a0+3.1415926*(math.exp(bi*math.cos(ai))+math.exp((-bi)*math.cos(ai)))*math.sin(ai)*0.1
		A = 1/a0
		A1 = 1/a0
		A2 = 1/a0

		frn = 0
		for a1i in a[:]:
			fa = (A/2)*(math.exp(bi*math.cos(a1i)) + math.exp(-bi*math.cos(a1i)))
			frn = frn+ui/q*kb*t*2*3.14*fa*math.log(fa)*0.1
		print(frn)

		ftn = 0
		for ci in c[:]:
			for a2i in a[:]:
				for a3i in a[:]:
					fa1 = 0.5*A1*(math.exp(bi*math.cos(a2i))+math.exp(-bi*math.cos(a2i)))
					fa2 = 0.5*A2*(math.exp(bi*math.cos(a3i))+math.exp(-bi*math.cos(a3i)))
					cosa1 = math.sin(a2i)*math.sin(a3i)*math.cos(ci) + math.cos(a2i)*math.cos(a3i)
					sina1 = math.sqrt(1-cosa1*cosa1)
					ftn = ftn + ui/q*kb*t*q*ui*(8*sina1*fa1*fa2*math.sin(a2i)*math.sin(a3i))*0.1*0.1*0.1
		
		ft = ftn + frn + ui/q*kb*t*math.log(ui/q)
		print(ft)

		if ftm > ft:
			ftm = ft

		print(ftm)




	all_ftm.append((ftm))

plt.figure()
plt.plot(all_u,all_f)
plt.plot(all_u, all_ftm)
plt.show()
