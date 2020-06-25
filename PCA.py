import numpy as np
import scipy as sp
from scipy import linalg as la
import matplotlib.pyplot as plt

datos=np.genfromtxt("siliconwaferthickness.csv", delimiter=",",skip_header=1)
G1=datos[:,0]
G2=datos[:,1]
G3=datos[:,2]
G4=datos[:,3]
G5=datos[:,4]
G6=datos[:,5]
G7=datos[:,6]
G8=datos[:,7]
G9=datos[:,8]


def normalizacion(array):
	x,y=np.shape(array)
	normal=np.zeros(np.shape(array))
	for i in range(y):
		normal[:,i]=(array[:,i]-np.mean(array[:,i]))/(np.std(array[:,i]))
	return normal

datos_normalizados=normalizacion(datos)



plt.plot(datos_normalizados)
plt.title("Datos normalizados")
plt.savefig("ExploracionDatos.pdf")
plt.close()

def promedio(datos_normalizados):
	return sum(datos_normalizados)/len(datos_normalizados)


def matrizdecov(datos_normalizados):
	x=len(datos_normalizados[0])
	covarianza=np.ones((x,x))
	for i in range(x):
		for j in range(x):
			x1=datos_normalizados[:,i]
			x2=datos_normalizados[:,j]
			
			y1=promedio(x1)
			y2=promedio(x2)
			
			cov=promedio((x1-y1)*(x2-y2))
			covarianza[i,j]=cov
	return covarianza

matriz=matrizdecov(datos_normalizados)
#print matriz

valores, vectores = la.eig(matriz) 
valores_ordenados=np.sort(valores)
vectores_ordenados=np.sort(vectores)

print valores_ordenados,vectores_ordenados

#Sacamos la variabilidad de los datos


for j in range(len(datos_normalizados[0])):
	variabilidad=[]
	suma=np.sum(valores_ordenados)
	variabilidad.append(valores_ordenados[j]/suma)

	print variabilidad

print "La cantidad de componentes principales para describir la variabilidad de los datos es una, dado que muestra una correlacion del 90,8% y la siguiente componente tiene una correlacion de 2,82% por lo tanto casi no esta relacionada como se mostro en la primera"


nueva_base=np.asarray(datos_normalizados)
grafica1=np.dot(nueva_base,vectores[0])
grafica2=np.dot(nueva_base,vectores[1])
plt.scatter(grafica2,grafica1)
plt.title('Graph of the normalized data in the reference system of the main components',fontsize=10)
plt.xlabel('Second principal component ')
plt.ylabel('First principal component')
plt.savefig("PCAdatos.pdf")
plt.close()

plt.scatter(vectores[0],vectores[1],color="purple")
plt.title("Agrupacion de las variables originales en el sistema de referencia de componentes principales", fontsize=10)
plt.show()































	

