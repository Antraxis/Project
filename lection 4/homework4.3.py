import random

one=[]
for lst in range(random.randint(3,10)):
    one.append(random.randint(0,50))
print(one)
result=[]
for two,u in enumerate(one):
    if two==1:
        y=one.copy()
        x=y.pop(0)
        result.append(x)
    elif two==2:
        y=one.copy()
        x=y.pop(2)
        result.append(x)
r=one.pop(-2)
result.append(r)
print(result)



