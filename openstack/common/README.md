# Description
This directory contains XMLs, scripts, user parameters for monitoring OpenStack systems.

# How to use
Link a template to a host, and set macros.

## Relations of emplates and hosts
* Template_OpenStack_Cinder.xml  
It provide a template "Template_OpenStack_Cinder". It enables monitoring Cinder nodes.

* Template_OpenStack_Common.xml  
It provide a template "Template_OpenStack_Common". It enables monitoring Linux system status.

* Template_OpenStack_Compute.xml  
It provide a template "Template_OpenStack_Compute". It enables monitoring Compute nodes.

* Template_OpenStack_Dashboard.xml  
It provide a template "Template_OpenStack_Dashboard". It enables monitoring Controller nodes executing Horizon.

* Template_OpenStack_Glance.xml  
It provide a template "Template_OpenStack_Glance". It enables monitoring Glance nodes.

* Template_OpenStack_Keystone.xml  
It provide a template "Template_OpenStack_Keystone". It enables monitoring Controller nodes executing Keystone.

* Template_OpenStack_MySQL.xml  
It provide a template "Template_OpenStack_MySQL". It enables monitoring Controller nodes executing MySQL.

* Template_OpenStack_Neutron_Controller.xml  
It provide a template "Template_OpenStack_Neutron_Controller". It enables monitoring Controller nodes executing Neutron Server.

* Template_OpenStack_Neutron_Network.xml  
It provide a template "Template_OpenStack_Neutron_Network". It enables monitoring Network nodes executing Neutron and Open vSwitch.

* Template_OpenStack_Nova_Controller.xml  
It provide a template "Template_OpenStack_Nova_Controller". It enables monitoring Controller nodes executing Nova.

* Template_OpenStack_Swift-Proxy.xml  
It provide a template "Template_OpenStack_Swift-Proxy". It enables monitoring Swift Proxy nodes.

* Template_OpenStack_Swift-Storage.xml  
It provide a template "Template_OpenStack_Swift-Storage". It enables monitoring Swift Storage nodes.


## Macros
* {$PRIVATE_IP}  
IP address for management port (192.168.0.x).

* {$PUBLIC_IP}  
IP address for public access port (10.0.0.x).

# Directories
* icehouse  
This directory contains XMLs for monitoring OpenStack Icehouse which were built according to the document by Virtual Tech Japan.  
http://enterprisecloud.jp/installguide-openstack/ (Select "Icehouse release" tab.)

* juno
This directory contains XMLs for monitoring OpenStack Juno which were built according to the document by Virtual Tech Japan.  
http://enterprisecloud.jp/installguide-openstack/ (Select "Juno release" tab.)

* */2.2
Later than MIRACLE ZBX / Zabbix version 2.2.

# License
GNU General Public License version 2