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
