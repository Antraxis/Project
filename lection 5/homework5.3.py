one = input("enter")
one_x= one.replace(".","").replace(",","").replace("!","").replace("?","").replace("'","")
separator=one_x.split()
try_2=""
for try_0 in separator:
      try_1=try_0.capitalize()
      try_2+=try_1
try_3="#"
summa=try_3+try_2
result=summa[:140]
print(result)