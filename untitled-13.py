def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-5)   
print my_abs(140)
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5,3)    
print power(6)
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n 
    return sum
#print calc([1,2,3])
#print calc((1,3,5,7))
print calc(1,2,3,4)
nums = [1,2,3]
print calc(*nums)
