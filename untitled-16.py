def f(x):
    return x * x

print map (f,[1,2,3,4,5,6,7,8,9]);

def add(x,y):
    return x + y
print reduce (add,[1,2,3,4,5])

def fn(x,y):
    return x * 10 + y
print reduce(fn,[1,2,3,4,5])

def is_odd(n):
    return n % 2 == 1
print filter(is_odd,[1,2,3,4,5])

def not_empty(s):
    return s and s.strip()

print filter(not_empty,['A','','B','',None,'C',' '])

def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36,56,78,412],reversed_cmp)