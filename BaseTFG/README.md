# RedTFG

//////////////////////////////////////////////////////////////


( El historial de commits del desarrollo de la fase previa se encuentran disponibles en el repositorio http://github.com/isabelplaza/PruebaINT.git )

Cualquier cambio en la maqueta requiere:

   1. make p4-build
   2. make app-build


Para arrancar la maqueta:
  
   1. $ make start-v4
      $ make app-reload
      $ make netcfg
   2. mininet> h1 ping h2 (y viceversa)
   3. $ make app-reload
   4. * mininet> h1 arp -i h1-eth0 -s 172.16.1.2 00:00:00:00:00:1B
      * mininet> h2 arp -i h2-eth0 -s 172.16.1.1 00:00:00:00:00:1A
      * mininet> h1 arp -i h1-eth0 -s 172.16.1.4 00:00:00:00:00:1D
      * mininet> collector arp -i collector-eth0 -s 172.16.1.1 00:00:00:00:00:1A
      * mininet> collector ping h1
      * mininet> h1 ping collector
      * mininet> h1 ping h2
      
      
      
## Puede que el ping no funcione ya que se han añadido cabeceras INT y el destinatario no reconozca ese formato nuevo de paquetes


Para poder tener comunicación IPv6:

   1. mininet> h1 ifconfig h1-eth0 inet6 add 2001:1:1::a/64
   2. mininet> h2 ifconfig h2-eth0 inet6 add 2001:1:1::b/64
   3. mininet> h1 ip -6 neigh replace 2001:1:1::B lladdr 00:00:00:00:00:1B dev h1-eth0
   4. mininet> h2 ip -6 neigh replace 2001:1:1::A lladdr 00:00:00:00:00:1A dev h2-eth0

Para poder ejecutar iperf:

   1. Añadir la siguiente línea antes del ultimo "make" en el fichero "./util/docker/stratum_bmv2/Dockerfile"
        iperf
   2. Ir al paso 4 del siguiente párrafo de instrucciones.
   3. util/mn-cmd h2
      iperf -s
   4. mininet> h1 iperf -c h2 -M 100



Estas son las instrucciones para tener en el contenedor Docker los ficheros de send.py y receive.py:

   1. Crear una carpera llamada "shared" en el directorio "./util/docker/stratum_bmv2/"
   2. Pegar en dicha carpeta la version definitiva de los ficheros send.py y receive.py. IMPORTANTE!!: Si se hace cualquier modificación, hay que recompilar la imagen de docker de nuevo (paso 4).
   3. Añadir la siguiente línea antes del ultimo COPY en el fichero "./util/docker/stratum_bmv2/Dockerfile"
        ADD ./shared /root
   4. Compilar la imagen de docker:
        cd ./util/docker/
        make build-stratum_bmv2
   5. Arrancar la maqueta en el directorio raíz del repositorio

Una vez arrancada la maqueta, ejecutar los comandos directamente en los hosts de mininet:

    cd <dir_raíz_repositorio>
    util/mn-cmd h2 python receive.py -c h2-eth0 # en un terminal
    util/mn-cmd h1 python send.py -e 00:00:00:00:00:1a,00:00:00:00:00:1b -i 172.16.1.1,172.16.1.2,0 -p 7000 -c h1-eth0 # en otro terminal
    util/mn-cmd h3 python send.py -e 00:00:00:00:00:1c,00:00:00:00:00:1c -i 172.16.1.3,172.16.1.2,0 -p 700 -c h3-eth0
    util/mn-cmd collector python send_col.py -e 00:00:00:00:00:1d,00:00:00:00:00:1a -i 172.16.1.4,172.16.1.1,0 -p 10 -c collector-eth0 -l # y el path
    util/mn-pcap h1
    

//////////////////////////////////////////////////////////////

Para pasar de docker al pc local
`docker exec 3a75e8b83993 cat timestamps_h1h2.txt > timestamps_100_20_h1h2`

////////////////////////////////////////////////////////////

Para capturar de manera adecuada 
`./mn-cmd collector python receiveh1.py -c collector-eth0`

`h1 ping -i 0.01 h2 -c 7000`
* Hay que acordarse de meter con arp tambien el h3 para que funcione el ping
