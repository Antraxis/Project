#one=[1,2,3,4,5,6]
#one=[1,2,3,4]
one=[1]
#one=[]
if len(one)==0:
    print([])
else:
    two=one.pop()
    one.insert(0,two)
    print(one)