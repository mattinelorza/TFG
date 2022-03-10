# Exercise 4: Enabling ONOS Built-in Services


# Part 1: Enable packet I/O and verify link discovery

## 1. Modify P4 program

* Hay que añadir los parametros necesarios para añadir funcionalidad a `packet-in/out`




### Set the packet egress port to that found in the cpu_out header
### 2. Remove (set invalid) the cpu_out header
### 3. Exit the pipeline here (no need to go through other tables

```p4

if (hdr.cpu_out.isValid()) {
            standard_metadata.egress_spec = hdr.cpu_out.egress_port;
            hdr.cpu_out.setInvalid();
            exit;
}

```

### 1. Set cpu_in header as valid
### 2. Set the cpu_in.ingress_port field to the original packet's ingress port (standard_metadata.ingress_port).

```p4

if (standard_metadata.egress_port == CPU_PORT) {
            

            hdr.cpu_in.setValid();
            hdr.cpu_in.ingress_port = standard_metadata.ingress_port;
            exit;
        }

```

## 2. Run PTF tests


```p4
"egress_port": outport,

```

```p4
self.insert(self.helper.build_table_entry(
            table_name="IngressPipeImpl.acl_table",
            match_fields={
                # Ternary match.
                "hdr.ethernet.ether_type": (eth_type, 0xffff)
            },
            action_name="IngressPipeImpl.clone_to_cpu",
            priority=DEFAULT_PRIORITY
        ))


```

```p4
"ingress_port": outport,

```


* los test PTF han funcionado correctamente


## 3. Modify ONOS pipeline interpreter

* Únicamente hay que poner el ingress_port y el egress_port

# COMANDOS INTERESANTES

## Comandos dentro de la CLI de ONOS

* Mostrar enlaces `links`
* Mostrar dispositivos `devices - s`

## Comandos dentro de el ONOS UI

* Mostrar etiquetas de los dispositivos `L`
* Hacer los hosts visibles `H`
* Igualar roles de master `E`


# PARTE 2 Host discovery & L2 bridging


* En caso de que no funcione es importante volver a hacer el make netcfg

* PASOS a seguir:
`make app-build`
`make app-reload`

## Se pueden observar las reglas aplicadas de la siguiente manera desde la onos-cli
* Para el leaf 1
`flows -s any:device:leaf1`

### Se verifica el correcto funcionamiento en el bridging l2 mediante un ping de h1a a h1b

### Desde onos con el comando `hosts -s` se observa como hay 2 hosts tras el ping anterior, lo mismo desde el onos ui pulsando la tecla `H`

