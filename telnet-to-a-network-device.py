#import required modules/packages/library
import pexpect

#define variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

#create telent session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

#check for error,if exists then display error and exit 
if result != 0:
    print('---FAILURE! creating session for: ', ip_address)
    exit()

#session is expecting username, enter details 
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

#check for error, if exists then display error and exit 
if result != 0:
    print('---FAILURE! entering username: ', username)
    exit()

#sesion is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

#check for error, if exists then display error and exit
if result != 0:
    print('---FAILURE! entering password: ', password)
    exit()

#display a success messgage if it works
print('-------------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('---               Username: ', username)
print('---               Password: ', password)
print('')
print('-------------------------------------------------')

#terminate telnet to device and close session.
session.sendline('quit')
session.close()