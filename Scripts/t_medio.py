#MATTIN A. ELORZA FORCADA

#Script para sacar tiempo medio de cada camino


from sys import argv
import numpy as np

arr = np.loadtxt(argv[1], dtype="int")


<<<<<<< HEAD
data = pd.DataFrame(arr)
res = pd.DataFrame(data.values[1::2]-data.values[::2])
res2= res.astype(int)
print(res2)


np.savetxt("resultados.csv",res2.astype(int),fmt='%i')


print(np.mean(res2))
=======

data = np.array(arr)
res = np.array(data[::2]-data[1::2])



np.savetxt("resultados.csv",res,fmt='%i')


print("Tiempo medio: %.2f ms" % (np.mean(res)/1000))
>>>>>>> 16853dc1d483058c063fc6582bd55a10d6379475
