import re

print('')
print('Devices and their Management IP addesses')
print('----------------------------------------')

ip_addr_pattern = re.compile(r'Mgmt:(\d{1,3}\.\d{1,3}\.\d{1,3})')
#read all lines of device info
file = open('devices-06.txt', 'r')
for line in file:
    device_info_list = line.strip().split(',')

device_info = {} #create the inner dictionary of device info
device_info['name'] = device_info_list[0]

#find the mgmt IP address from the line in the file
mgmt_addr = ip_addr_pattern.search(line)
device_info['ip'] = mgmt_addr.group(1)

#display device and management IP address
print(' Device:', device_info['name'], 'Mgmt IP:', device_info['ip'])

print('')
file.close()