## Siempre que se hagan cambios en un fichero que vaya en /util

Desde /RedTFG/util/docker hay que compilar la imagen de docker

* `make build-stratum_bmv2`


## Cualquier cambio en la maqueta

* `make p4-build`
* `make app-build`

## Para Arrancar la máquina del TFG

* `make start-v4`

Ejecutar `make onos-log`para observar que todo ha ido bien y esperar a que termine.

* `make app-reload`
* `make netcfg`



# Mininet 
Para arrancar terminal de Mininet `make mn-cli` 

* `h1 ping h2`
* `h2 ping h1`
* `h3 ping h2`
* `h2 ping h3`
* `h1 ping collector`
* `collector ping h1`

De esta manera los equipos se descubrirán entre sí.






