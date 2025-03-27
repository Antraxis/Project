#one=[0, 1, 0, 12, 3]
#one=[1, 0, 13, 0, 0, 0, 5]
one=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#one=[0]
for two in one:
    if two==0:
        u=one.index(two)
        y=one.pop(u)
        one.append(y)
print(one)

