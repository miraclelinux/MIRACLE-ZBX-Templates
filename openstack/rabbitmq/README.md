# Description
This directory contains XMLs, scripts, user parameters for monitoring RabbitMQ on OpenStack systems.

# How to use
Copy all files and Link a template to a host executing RabbitMQ.

## Directories
* XMLs/2.2  
This directory contains a XML for MIRACLE ZBX / Zabbix later than version 2.2.

* etc  
This directory contains scripts, user parameters, etc. Put all files to your Controller node, keeping the directory tree.

## Files
* /etc/sudoers.d/zbx_rabbitmqctl:  
set owner and group as root, mode as 440

* /etc/zabbix/rabbitmq.queue.num:  
set owner and group as root, mode as 755

* /etc/zabbix/zabbix_agentd.conf.d/rabbitmq:  
set owner and group as root, mode as 644

# Key of item
## rabbitmq.queue.num[&lt;filter&gt;,&lt;queueinfoitem&gt;]

* filter  
Set a name of rabbitmq list.
Default: (none)

* queueinfoitem  
Set a string from following: messages_ready, messages_unacknowledged, messages  
Default: messages

# Requires
Python

# License
GNU General Public License version 2
