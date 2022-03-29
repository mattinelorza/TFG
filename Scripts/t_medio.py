#MATTIN A. ELORZA FORCADA

#Script para sacar tiempo medio de cada camino


from sys import argv
import pandas as pd
import numpy as np

arr = np.loadtxt(argv[1], dtype="int")

print(arr)

data = pd.DataFrame(arr)
res = pd.DataFrame(data.values[::2]-data.values[1::2])
res2= res.astype(int)
print(res2)

np.savetxt("resultados.csv",res2.astype(int),fmt='%i')


