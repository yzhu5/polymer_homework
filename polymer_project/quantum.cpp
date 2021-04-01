#include<iostream>
/*
*find nine values with their summation of its square equal 500. 
i*/
int getOMGA(int i, int j, int k);
int combination(int m, int n);
int factorial(int i);

int main()
{
	//set parameters nx, ny, nz
	int nx=0, ny=0, nz=0;
	int E=0;
	int graph[500];
	for(int i=0; i<500; i++)
		graph[i]=0;
	//only have one parameters nx
	nx=1;
	E=9*nx*nx;
	while(E<=500)
	{
		graph[E-1]=1;
		nx++;
		E=9*nx*nx;
	}	
	//have more parameters nx,ny,nz
	for(int i=1; i<9; i++)
	{	
		for(int j=1; j<=(9-i); j++)
		{
			for(nx=1; nx<23; nx++)
			{
				for(ny=1+nx; ny<23; ny++)
				{
					for(nz=1+ny; nz<23; nz++)
					{
						E=i*nx*nx+j*ny*ny+(9-i-j)*nz*nz;
		                                if(E<=500)
        		                        	graph[E-1]=getOMGA(i, j , 9-i-j);
					}
				}
			}
		}
	}	

	//output data
	for(int n=8; n<500; n++)
		std::cout << n+1 << " value is " << graph[n]<<std::endl;
	
	return 0;
}

//calculate OMGA
int getOMGA(int i, int j, int k)
{
	if(k==0)
		return combination(9, j);
	else
		return combination(9, j)* combination(9-j, k);
}

//calculate combination Cmn
int combination(int m, int n)
{
	return factorial(m)/(factorial(n)*factorial(m-n));
}

//calculate factorial
int factorial(int i)
{	
	int F=1;
	for(int m=1; m<i+1; m++)
		F*=m;
	return F; 
}



