S = 'abcdefghijk'#range函数处理字符串
for i in range(0,len(S),2):
    print S[i]
S = 'abcdefhijkl'
for (index,char) in enumerate(S):#enumerate键值对
    print index 
    print char
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):#zip函数聚合列表
    print(a,b,c)
ta = [1,2,3]
tb = [9,8,7]
zipped = zip(ta,tb)
print(zipped)
#decompose
na, nb = zip(*zipped)#没加变量是一个值,加了是一组值.
print(na, nb)
func = lambda x,y: x + y#成为,转到
print func(3,4)
def test(f,a,b):
    print 'test'
    print f(a,b)
test(func,3,5)
re = map((lambda x:x+3),[1,3,5,6])
for i in re:
    print i
    