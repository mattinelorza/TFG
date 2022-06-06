# Script para tomar decisiones acerca de que camino escoger
# Author: MATTIN A. ELORZA FORCADA

#from decimal import Subnormal
from sys import argv
import numpy as np
import subprocess


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

subprocess.run('./mn-cmd', 'h1', 'python', 'caminorecv.py', '-c h1-eth0')

if(t_medio2 <= t_medio1*0.95):
    print("Camino Optimo 2")
    camino = 2
else: 
    print("Camino Optimo 1")
    camino = 1

subprocess.run('./mn-cmd', 'collector', 'python', 'send_col.py', '-e 00:00:00:00:00:1d,00:00:00:00:00:1a', '-i 172.16.1.4,172.16.1.1,0', '-p 1', '-c collector-eth0', '-l ' + str(camino))

