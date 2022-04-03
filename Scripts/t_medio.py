#MATTIN A. ELORZA FORCADA

#Script para sacar tiempo medio de cada camino


from sys import argv
import numpy as np

arr = np.loadtxt(argv[1], dtype="int")



data = np.array(arr)
res = np.array(data[::2]-data[1::2])



np.savetxt("resultados.csv",res,fmt='%i')


print("Tiempo medio: %.2f ms" % (np.mean(res)/1000))