import getpass
from netmiko import ConnectHandler
username=raw_input(":username")
password=getpass.getpass("password")
cisco_881 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.40.2',
    'username': username ,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
}
net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_command('show ip int brief')
print(output)
