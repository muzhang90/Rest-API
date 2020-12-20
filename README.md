# REST API

REST API is disabled on Junos devices by default.  Need to add below config to enable REST API function:

set system services rest http
set system services rest enable-explorer

Once above config is commited, could use HTTP to manage device with help of REST API. 
