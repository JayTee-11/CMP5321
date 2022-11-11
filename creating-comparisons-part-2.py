#display heading
print('')
print('Devices with bad software versions')
print('----------------------------------')

current_version = 'Version 5.3.1'

#read all lines of device information from file
file = open('devices-06.txt', 'r')

for line in file:
    #put device info into list
    device_info_list = line.strip().split(',')

#put device information into dictionary for this one device
device_info = {} #create the inner dictionary of device info
device_info ['name'] = device_info_list[0]
device_info ['ip'] = device_info_list[2]
device_info ['version'] = device_info_list[3]

#if the device doesn't match our 'current version',
#display a warning
if device_info ['version'] != current_version:
    print(' Device:', device_info['name'],
    'version:', device_info['version'])

#display a blank line to make easier  to read
print('')

file.close()