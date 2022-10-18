#import required modules/packages/library
import pexpect

#define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

#create the ssh session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['password:', pexpect.TIMEOUT, pexpect.EOF])

#check for errors, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

#session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

#check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()

#Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMOUT, pexpect.EOF])

#check for error, if exists then display error and exit
if result != 0:
    print('--- FAULURE! entering config mode')
    exit()

#change the hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

#check for error, if it exists then display error and exit
if result != 0:
    print('--- Failure! setting hostname')

#exit config mode
session.sendline('exit')

#exit enable mode
session.sendline('eixt')

#display success message if works
print('------------------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('---              Username: ', username)
print('---              password: ', password)
print('')
print('------------------------------------------------------')

#terminate SSH session
session.close()

