# Description
This directory contains XMLs, scripts, user parameters for monitoring network traffic in namespace on Network node of OpenStack.

# How to use
Copy all files and Link a template to a host. Items will be set automatically by "Discovery" function.

## Directories
* XMLs/2.2  
This directory contains a XML for MIRACLE ZBX / Zabbix later than version 2.2.

* etc  
This directory contains scripts, user parameters, etc. Put all files to your Controller node, keeping the directory tree.

## Files
* /etc/sudoers.d/zbx_netns:  
set owner and group as root, mode as 440

* /etc/zabbix/netns.net.if:  
set owner and group as root, mode as 755

* /etc/zabbix/netns.net.if.discovery:  
set owner and group as root, mode as 755

* /etc/zabbix/zabbix_agentd.conf.d/netns:  
set owner and group as root, mode as 644


# Key of item
## netns.net.if.discovery
Returns combinations of namespace and interfaces with JSON.

## netns.net.if.in[&lt;if&gt;,&lt;mode&gt;,&lt;namespace&gt;]
Returns incomming traffic statistics on assigned interface and namespace.  

* if  
network interface name

* mode  
bytes: number of bytes (default)  
dropped: number of dropped packets  
errors: number of errors  
overruns: number of overruns  
frame: number of frame packets  
multicast: number of multicast packets  
packets: number of packets  
compressed: number of compressed packets

* namespace  
name of namespace

## netns.net.if.out[&lt;if&gt;,&lt;mode&gt;,&lt;namespace&gt;]
Returns outgoing traffic statistics on assigned interface and namespace.  

* if  
Interface
network interface name

* mode  
bytes: number of bytes (default)  
dropped: number of dropped packets  
errors: number of errors  
overruns: number of overruns  
packets: number of packets  
carrier: number of carrier packdts  
compressed: number of compressed packets  

* namespace  
name of namespace

# netns.net.if.collisions[&lt;if&gt;,&lt;namespace&gt;]
Returns number of collisions on assigned interface and namespace.

# Requires
Python

# License
GNU General Public License version 2
