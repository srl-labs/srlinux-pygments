# SR Linux Pygments Demo

## Basic CLI snippet

```srlmin
# some comment
    
--{ +* candidate shared default }--[ routing-policy ]--
A:leaf1# info
    policy all {
        default-action {
            policy-result accept
        }
    }
    
```

```srl
--{ * candidate shared default }--[ system event-handler instance opergroup ]--
A:leaf1# info
    paths [
        "interface ethernet-1/{49..50} oper-state"
    ]
```

```srl
--{ * candidate shared default }--[ network-instance black ]--
A:leaf1# info static-routes
        static-routes {
            route 192.168.18.0/24 {
                admin-state enable
                metric 1
                preference 5
                next-hop-group static-ipv4-grp
            }
            route 2001:1::192:168:18:0/64 {
                admin-state enable
                metric 1
                preference 6
                next-hop-group static-ipv6-grp
            }
        }
```

```srl
--{ show }--
A:leaf1# show network-instance default interfaces
===================================================================
Net instance    : default
Interface       : ethernet-1/1.1
Oper state      : up
Ip mtu          : 1500
                  Prefix                      Origin        Status
  =================================================================
  192.35.1.0/31                             static
  2001:192:35:1::/127                       static       preferred
  fe80::201:5ff:feff:0/64                   link-layer   preferred
===================================================================
Net instance    : default
Interface       : lo0.1
Oper state      : up
                  Prefix                      Origin        Status
  =================================================================
  5.5.5.5/32                                static
  2001:5:5:5::5/128                         static       preferred
===================================================================

```

## Set style

```srl
enter candidate

# configuration of the physical interface and its subinterface
set / interface ethernet-1/49 subinterface 0 ipv4 address 192.168.11.1/30

# system interface configuration
set / interface system0 subinterface 0 ipv4 address 10.0.0.1/32

# routing policy
set / routing-policy policy all default-action policy-result accept

# BGP configuration
set / network-instance default protocols bgp autonomous-system 101
set / network-instance default protocols bgp router-id 10.0.0.1
set / network-instance default protocols bgp neighbor 192.168.11.2 peer-group eBGP-underlay

commit now
```

## Show commands

```srl
--{ + running }--[  ]--
A:spine1# show network-instance default protocols bgp neighbor
----------------------------------------------------------------------------------------------------------------------------------------------
BGP neighbor summary for network-instance "default"
Flags: S static, D dynamic, L discovered by LLDP, B BFD enabled, - disabled, * slow
----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------
+----------------+-----------------------+----------------+------+---------+-------------+-------------+-----------+-----------------------+
|    Net-Inst    |         Peer          |     Group      | Flag | Peer-AS |    State    |   Uptime    | AFI/SAFI  |    [Rx/Active/Tx]     |
|                |                       |                |  s   |         |             |             |           |                       |
+================+=======================+================+======+=========+=============+=============+===========+=======================+
| default        | 192.168.11.1          | eBGP-underlay  | S    | 101     | established | 0d:18h:20m: | ipv4-unic | [2/1/4]               |
|                |                       |                |      |         |             | 49s         | ast       |                       |
| default        | 192.168.12.1          | eBGP-underlay  | S    | 102     | established | 0d:18h:20m: | ipv4-unic | [2/1/4]               |
|                |                       |                |      |         |             | 9s          | ast       |                       |
+----------------+-----------------------+----------------+------+---------+-------------+-------------+-----------+-----------------------+
----------------------------------------------------------------------------------------------------------------------------------------------
Summary:
2 configured neighbors, 2 configured sessions are established,0 disabled peers
0 dynamic peers
```

```srl
--{ + running }--[  ]--                             
A:spine1# show interface ethernet-1/1               
====================================================
ethernet-1/1 is up, speed 10G, type None
  ethernet-1/1.0 is up
    Network-instance: 
    Encapsulation   : null
    Type            : routed
    IPv4 addr    : 192.168.11.2/30 (static, None)
----------------------------------------------------
====================================================
```

```srl
--{ + running }--[  ]--
A:leaf1# show network-instance default protocols bgp summary
-------------------------------------------------------------
BGP is enabled and up in network-instance "default"
Global AS number  : 101
BGP identifier    : 10.0.0.1
-------------------------------------------------------------
  Total paths               : 3
  Received routes           : 3
  Received and active routes: None
  Total UP peers            : 1
  Configured peers          : 1, 0 are disabled
  Dynamic peers             : None
-------------------------------------------------------------
Default preferences
  BGP Local Preference attribute: 100
  EBGP route-table preference   : 170
  IBGP route-table preference   : 170
-------------------------------------------------------------
Wait for FIB install to advertise: True
Send rapid withdrawals           : disabled
-------------------------------------------------------------
Ipv4-unicast AFI/SAFI
    Received routes               : 3
    Received and active routes    : None
    Max number of multipaths      : 1, 1
    Multipath can transit multi AS: True
-------------------------------------------------------------
Ipv6-unicast AFI/SAFI
    Received routes               : None
    Received and active routes    : None
    Max number of multipaths      : 1,1
    Multipath can transit multi AS: True
-------------------------------------------------------------
EVPN-unicast AFI/SAFI
    Received routes               : None
    Received and active routes    : None
    Max number of multipaths      : N/A
    Multipath can transit multi AS: N/A
-------------------------------------------------------------
```

```srl
A:srl2# /show network-instance default protocols ldp ipv4 fec                                     
==================================================================================================
Net-Inst default LDP IPv4: All FEC prefixes table
==================================================================================================
Received FEC prefixes
--------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------------------+
| FEC prefix           Peer LDP ID                 Label                Ingress   Used in    |
|                                                                       LSR       Forwarding |
+============================================================================================+
| 10.0.0.1/32          10.0.0.1:0                  100                  true      true       |
| 10.0.0.1/32          10.0.0.3:0                  304                  true      false      |
| 10.0.0.3/32          10.0.0.1:0                  109                  true      false      |
| 10.0.0.3/32          10.0.0.3:0                  300                  true      true       |
+--------------------------------------------------------------------------------------------+
--------------------------------------------------------------------------------------------------
Advertised FEC prefixes
--------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------------------+
| FEC prefix           Peer LDP ID                 Label                Label        Egress  |
|                                                                       Status       LSR     |
+============================================================================================+
| 10.0.0.1/32          10.0.0.3:0                  206                               false   |
| 10.0.0.2/32          10.0.0.1:0                  204                               true    |
| 10.0.0.2/32          10.0.0.3:0                  204                               true    |
| 10.0.0.3/32          10.0.0.1:0                  205                               false   |
+--------------------------------------------------------------------------------------------+
--------------------------------------------------------------------------------------------------
Total received FEC prefixes  : 4 (2 used in forwarding)
Total advertised FEC prefixes: 4

```

## Comments

```srl
# some comment starting at the beginning of a line
 # comment starting not at the beginning
# 
#

--{ * candidate shared default }--[ network-instance default protocols bgp ]--
A:leaf1# /routing-policy
```
