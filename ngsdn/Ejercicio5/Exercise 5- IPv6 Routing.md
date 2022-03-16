# Exercise 5: IPv6 Routing

### Requirements

At this stage, we want our fabric to behave like a standard IP fabric, with
switches functioning as routers. As such, the following requirements should be
satisfied:

* Leaf interfaces should be assigned with an IPv6 address (the gateway address)
  and a MAC address that we will call `myStationMac`;
* Leaf switches should be able to handle NDP Neighbor Solicitation (NS)
  messages -- sent by hosts to resolve the MAC address associated with the
  switch interface/gateway IPv6 addresses, by replying with NDP Neighbor
  Advertisements (NA) notifying their `myStationMac` address;
* Packets received with Ethernet destination `myStationMac` should be processed
  through the routing tables (traffic that is not dropped can then be
  processed through the bridging tables);
* When routing, the P4 program should look at the IPv6 destination address. If a
  matching entry is found, the packet should be forwarded to a given next hop
  and the packet's Ethernet addresses should be modified accordingly (source set
  to `myStationMac` and destination to the next hop one);
* When routing packets to a different leaf across the spines, leaf switches
  should be able to use ECMP to distribute traffic.


## El fichero netcfg.json se encuentra en /mininet


* Como es esperado tras hacer el ping no hay conectividad entre el h2 y el h3

# Hay que modificar el programa P4

* Parte del TODO del ejercicio 5 nos lo dan dentro de snippets.p4 con la acción `ndps_ns_to_na`

## Errores previos en los test

Could not find 'IngressPipeImpl.my_station table'

Could not find 'IngressPipeImpl.ndp_reply_table'

# SE HAN CORREGIDO Y EL CÓDIGO FUNCIONA CORRECTAMENTE

