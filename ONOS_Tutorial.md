# REVISIÓN DE TUTORIALES 5-IV-2022

* ONOS

El ping puede que no funcione de primeras, esto es debido a que en el plano de datos los flujos no estan bien instalados.

ONOS provee de una aplicacioón que no viene activada por defecto llamada `Reactive Forwarding` 

## ¿ Como ver las apps activas?
`apps -a -s`

## Activar el forwarding 
`app activate org.onosproject.fwd` también vale `app activate fwd`

## Listar dispositivos activos
`devices`

## Listar enlaces detectados por ONOS
`links`

## Listar equipos del sistema
`hosts`
Añadiendo la opción `-s` da información más detallada

## Listar flujos registrados en el sistema
`flows`

## Listar las rutas mas cortas
`paths <TAB>` 

## Ver las rutas gráficamente en ONOS entre equipos
Desde el onos-gui seleccionando el switch deseado y `V` 

### Para más ayuda, pulsar la tecla `/` desde el GUI

## Mostrar el tráfic en ONOS
mininet> `bgIperf h1 h2`
En caso de querer observar las estadísticas de cada flujo `A`

# COSAS DE INTERES

* instalar el CPMan (Control Plane Manager)