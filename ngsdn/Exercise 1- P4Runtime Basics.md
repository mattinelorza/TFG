

# He terminado el ejercicio aunque daba un error el .py al asignarle el puerto

## What is the fully qualified name of the l2_exact_table? What is its numeric ID?

```

Name: "IngressPipeImpl.l2_exact_table"
alias: "l2_exact_table"
ID: 33605373

```

## To which P4 entity does the ID 16812802 belong to? A table, an action, or something else? What is the corresponding fully qualified name?

```
name: IgressPipeImpl.set_egress_port
alias: set_egress_port

```

* Se trata de una acción


## For the IngressPipeImpl.set_egress_port action, how many parameters are defined for this action? What is the bitwidth of the parameter named port_num?

* Hay 1 parametro definido para dicha acción:

```
id: 1
name: "port_num"
bitwidth: 9

```

## At the end of the file, look for the definition of the controller_packet_metadata message with name packet_out at the end of the file. Now look at the definition of header cpu_out_header_t in the P4 program. Do you see any relationship between the two?

* En el p4 info se hace referencia en la anotación a la cabecera del programa principal.

