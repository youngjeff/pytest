import math

def move(x,y,step, angle=0):
    nx = x + step * math.cos(angle)
    ny = x - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print x,y

r = move(100,100,60,math.pi/6)
print r 
def enroll(name,gender):
    print 'name',name
    print 'gender',gender
enroll('Sarah','F')
def enrolls(name,gender,age=6,city='Beijing'):
    print 'name:',name
    print 'gender',gender
    print 'age:',age
    print 'city:',city
enrolls('Sarah','F')
def cals(*number):#未知数未定，×
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
#print cals(1,2)
nums = [1,2,3]
print cals(*nums)
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw
print person('Michael',30)
print person('Bob',35,city='Beijing')
print person('Adam',45,gender='M',job='Engineer')
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
func(1,2)    
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=66)
args = (1,2,3,4)
kw = {'X':99}
func(*args,**kw)
