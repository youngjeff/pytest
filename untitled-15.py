def fact(n):
    if n ==1:
        return 1
    return n * fact(n - 1)
print fact(3)
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
#print L    
print L[1:3]
print L[:10]
print L[-10:]
Ls = range(100)
#print Ls
d = {'a':1,'b':2,'c':3}
for key in d:
    print key
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)
L = []
for x in range(1,11):
    L.append(x * x)
print L
L = ['Hello','World','IBM','Apple']
print [s.lower() for s in L]
print [x * x for x in range(1,11)]
print [m + n for m in 'ABC' for n in 'XYZ']
d = {'x':'A','y':'B','z':'C'}
for k,v in d.iteritems():
    print k,'=',v
import os
print [d for d in os.listdir('.')]


    