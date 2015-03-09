# Description
These XMLs enable monitoring with SSH instead of Zabbix Agent.

# How to use
Link a template to a host, and set macros.

## Macros
### Templates_*_SSH_Passphrase
* {$SSH_USER}  
A login user.

* {$SSH_PRIVATE_KEY}  
PAHT to "Private key" file on Zabbix Server.

* {$SSH_PUBLIC_KEY}  
PAHT to "Public key" file on Zabbix Server.

* {$SSH_PASSPHRASE}   
The passphrase of private key file.

* {$SSH_ENCODING}  
The encode if you use except UTF-8.

* {$SSH_PORT}  
A port number if you use except 22.


### Templates_*_SSH_Password
* {$SSH_USER}  
A login user.

* {$SSH_PASSWD}  
The password of login user.

* {$SSH_PORT}  
A port number if you use except 22.

* {$SSH_ENCODING}  
The encode if you use except UTF-8.


# Directories
* 1.8  
Later than MIRACLE ZBX / Zabbix version 1.8.

# Files
* Template_Linux_SSH_Passphrase.xml  
It provide a template "Template_Linux_SSH_Passphrase". It enables monitoring Linux systems with information of user/passphrase.

* Template_Linux_SSH_Password.xml  
It provide a template "Template_Linux_SSH_Passphrase". It enables monitoring Linux systems with information of user/password.

* Template_Solaris10_SSH_Passphrase.xml  
It provide a template "Template_Solaris10_SSH_Passphrase". It enables monitoring Solairs 10 systems with information of user/passphrase.

* Template_Solaris10_SSH_Password.xml  
It provide a template "Template_Solaris10_SSH_Passphrase". It enables monitoring Solaris 10 systems with information of user/password.

# License
GNU General Public License version 2