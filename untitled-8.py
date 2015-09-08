def func(*name):
    print type(name)
    print name
    
func(1,4,3)
func(5,8,9,7,5,4)#这是一个包裹,他是一个元组,参数并不固定.
def func(**dict):
    print type(dict)
    print dict

func(a=1,b=9)
func(m=2,n=1,c=11)