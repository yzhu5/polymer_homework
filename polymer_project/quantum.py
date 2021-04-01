import matplotlib.pyplot as plt

def getOMGA(i, j, k):
        if k==0:
                return combination(9, j)
        else:
                return combination(9, j)* combination(9-j, k)

def combination(m, n):
        return factorial(m)/(factorial(n)*factorial(m-n))


def factorial(i):
        F=1
        for m in range(1, i+1): 
                F*=m
        return F

def Do():
	nx=0
	ny=0
	nz=0
	E=0
	graph=[]
	for i in range (0, 500):
		graph.append(0)
	
	nx=1
	E=9*nx*nx
	while E<=500:
		graph[E-1]=1
		nx+=1
		E=9*nx*nx
	
	for i in range (1,9):	
		for j in range (1,9-i+1):
			for nx in range (1,23):
				for ny in range (1+nx, 23):
					for nz in range (1+ny, 23):
						E=i*nx*nx+j*ny*ny+(9-i-j)*nz*nz
						if E<=500:
							graph[E-1]=getOMGA(i, j , 9-i-j)


	x=[]
	for n in range (0, 500):
		print( n+1 ," value is " ,graph[n])
		x.append(n)

	plt.plot(x, graph)
	plt.show()


Do()
