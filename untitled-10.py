permissions = 'rw'
asd = 'w' in permissions 
print asd
sda = 'x' in permissions 
print sda
users = ['min','foo','bar']
asda = raw_input('Enter your user name:') in users
print asda
database = [
['albert','1234'],
['dilbert','4242'],
['smith','7524'],
['jones','9843']
]
username = raw_input('User name: ')
pin = raw_input('Pin code:')
if [username,pin] in database:
 print 'Access granted'
else:print 'cannot'