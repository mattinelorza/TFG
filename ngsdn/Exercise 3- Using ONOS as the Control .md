# Exercise 3: Using ONOS as the Control Plane

## Comandos útiles

### Para reiniciar los contenedores de ONOS y Mininet eliminando previos estados

```
make restart
```
### Para observar los LOGs de  ONOS

``` 
make onos-log
``` 
### Iniciar interfaz de linea de comandos onos

```
make onos-cli
```

### Mostrar aplicaciónes en funcionamiento

```
apps -a -s
```

### Salir del cli de ONOS 
 
```
Ctrl-D
```

## Comprobar configuración

```
onos> devices -s
```
* deberán de aparecer todos como available=true

# ONOS

<http://127.0.0.1:8181/onos/ui>

username `onos`, password `rocks`

* Mostrar etiquetas de dispositivos:
```
L
```
* Información sobre la ONOS web UI
<https://wiki.onosproject.org/x/OYMg>
