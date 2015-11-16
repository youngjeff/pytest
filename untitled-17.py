def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n 
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print f()
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
def now():
    print '2013-12-25'
 
f =now
f()
print f.__name__
def int2(x,base=2):
    return int(x,base)  
print int2('100000')
import functools
int3 = functools.partial(int,base=2)
print int3('1100000')
max2 = functools.partial(max,1000)
print max2(5,6,7)