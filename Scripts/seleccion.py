#MATTIN A. ELORZA FORCADA

#Script para tomar decisiones acerca de que camino escoger


from sys import argv
import numpy as np

arr = np.loadtxt(argv[1], dtype="int")
arr2= np.loadtxt(argv[2], dtype="int")


data = np.array(arr)
res = np.array(data[::2]-data[1::2])

data1=np.array(arr2)
res2 = np.array(data1[::2]-data1[1::2])


np.savetxt("resultados1.csv",res,fmt='%i')
np.savetxt("resultados2.csv",res,fmt='%i') #no creo que interese crear los ficheros

t_medio1=np.mean(res)
t_medio2=np.mean(res2)
print("Tiempo medio H1-H2: %.2f ms" % (t_medio1/1000))
print("Tiempo medio H3-H2: %.2f ms" % (t_medio2/1000))

if( t_medio2 <= t_medio1*0.95 ):
    print("Camino Optimo 2")
else: print("Camino Optimo 1")
