one=[0, 1, 7, 2, 4, 8]
#one=[1, 3, 5]
#one=[6]
#one=[]
if len(one)==0:
    print(0)
else:
    two=one[::2]
    one.reverse()
    u=one.pop(0)
    y=sum(two)
    print(y*u)