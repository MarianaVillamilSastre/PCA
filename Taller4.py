import numpy as np
import scipy as sp
from scipy import linalg as la
import matplotlib.pyplot as plt


DataCredit=np.genfromtxt("DataCredit.csv")

filas=np.shape(DataCredit[:,0])
print filas
columnas=np.shape(DataCredit[0,:])
print columnas


for i in range(0,7):
	
	DataCredit[:,i]=((DataCredit[:,i]-np.mean(DataCredit[:,i]))/np.std(DataCredit[:,i]))
		
	matrizdecov=np.cov(DataCredit)
	print matrizdecov

[valores,vectores]=la.eig(matrizdecov)
valores1=-np.sort(-valores[0:7])
plt.plot(valores1)
plt.show()
for j in range(0,7):
	variabilidad=valores1[0]+valores1[1]+valores1[2]+valores1[3]
	suma=sum(np.sort(valores[0:400]))
	variabilidad1=variabilidad/suma
	
	print variabilidad1


