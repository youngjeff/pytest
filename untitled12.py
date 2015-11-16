classmates = ['michcal','bob','tracy']
print classmates
print len(classmates)
classmates.append('adam')
print classmates
classmates.pop(1)
print classmates
mates = ('Michael','Bob','Tracy')
age = 3
if age >= 18:
    print 'your age is ',age
    print 'adult'
elif age <=6:
    print 'your age is ',age
    print 'teenager'
else:
    print 'kid'
names = ['Michael','Bob','Tracy']
for name in names:
    print name
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x 
print sum
sums = 0
for x in range(101):
    sums += x
print sums
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum    
#births = int(raw_input('births:\n'))
#if births < 2000:
    #print '00前'
#else:
    #print '00后'
d = {'Michael':95,'Bob':75,'Tracy':85}
print d['Michael']
print 'Thomas' in d 
print d.get('Thomas')
print d.get('Thomas',-1)
s = set([1,2,3])
print s
s.add(4)
print s
s.remove(4)
print s
s2 = set([2,3,4])
print s & s2
print s | s2
a = 'abc'
b = a.replace('a',"A")
print b
print float('123.2123')
print str(1.23)
print unicode(100)
print bool(0)
a = abs
print a(-456)

  
        