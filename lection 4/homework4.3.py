#one=[1, 2, 3, 4, 5, 6, 7, 9]
one=[1, 1, 2, 1]
#one=[6, 3, 7]
good=[]
for two,u in enumerate(one):
    if two==1:
        y=one.copy()
        x=y.pop(0)
        good.append(x)
        continue
    elif two==2:
        y=one.copy()
        x=y.pop(2)
        good.append(x)
r=one.pop(-2)
good.append(r)
print(good)



