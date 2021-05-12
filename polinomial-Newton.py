import numpy as np
import numpy as poly
x = np.array([-1,0,1,3], dtype="double")
y = np.array([3,1,3,43], dtype="double")
  #inicializando a tabela  
T = np.zeros((4,4));  
#primeira coluna  
T[:,0]=y;  
#segunda coluna  
T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0]);  
T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1]);  
T[3,1]=(T[3,0]-T[2,0])/(x[3]-x[2]);  
#terceira coluna  
T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0]);  
T[3,2]=(T[3,1]-T[2,1])/(x[3]-x[1]);  
#quarta coluna  
T[3,3]=(T[3,2]-T[2,2])/(x[3]-x[0]);  
print(T)  #polinomio interpolador  
p = np.array([T[0,0]], dtype="double")  
paux = np.array([-x[0],1], dtype="double")