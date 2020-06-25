import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

matriz_velocidad=np.array([[4,2,1,45.948],[25,5,1,119.985],[81,9,1,231.497]])


def eliminacion_gaussiana():
	for i in range(len(matriz_velocidad)):
		if(i==0):
			matriz_velocidad[0,:]=matriz_velocidad[0,:]/matriz_velocidad[0,0]
			matriz_velocidad[1,:]=matriz_velocidad[1,:]-(matriz_velocidad[1,0])*matriz_velocidad[0,:]
			matriz_velocidad[2,:]=matriz_velocidad[2,:]-(matriz_velocidad[2,0])*matriz_velocidad[0,:]
		elif(i==1):
			matriz_velocidad[1,:]=matriz_velocidad[1,:]/matriz_velocidad[1,1]
			matriz_velocidad[2,:]=matriz_velocidad[2,:]-(matriz_velocidad[2,1])*matriz_velocidad[1,:]
			matriz_velocidad[0,:]=matriz_velocidad[0,:]-(matriz_velocidad[0,1])*matriz_velocidad[1,:]
		elif(i==2):
			matriz_velocidad[2,:]=matriz_velocidad[2,:]/matriz_velocidad[2,2]
			matriz_velocidad[0,:]=matriz_velocidad[0,:]-(matriz_velocidad[0,2])*matriz_velocidad[2,:]
			matriz_velocidad[1,:]=matriz_velocidad[1,:]-(matriz_velocidad[1,2])*matriz_velocidad[2,:]
	return matriz_velocidad

matriz_velocidad2=[]
matriz_velocidad2=eliminacion_gaussiana()

a1=matriz_velocidad2[0,3]
a2=matriz_velocidad2[1,3]
a3=matriz_velocidad2[2,3]

t=np.linspace(0,10,100)
velocidad=(a1*t**2) + a2*t + a3
g1=plt.plot(t,velocidad,label='Polinomio con sus respectivos coeficientes')
plt.scatter([2],[45.948])
plt.scatter([5],[119.985])
plt.scatter([9],[231.497])
plt.title('Spaceship velocity')
plt.xlabel('Time(s)')
plt.ylabel('Distance (m)')
plt.savefig('VelocidadCohete.pdf')
plt.close()

print "Los coeficientes encontrados por el metodo son:",a1,a2,a3
velocidad7=(a1*7**2) + a2*7 + a3
print "El valor de la velocidad en t=7 es :",velocidad7,"m/s"






