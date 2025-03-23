num_1=int(input('number1'))
effect =input('effect')
num_2=int(input('number2'))
if effect == '+':
   print(int(num_1 + num_2))
elif effect == '-':
    print(int(num_1-num_2))
elif effect=='*':
    print(int(num_1*num_2))
elif effect == '/':
     if num_2 == 0 or num_1 == 0:
            print('Это невозможно')
     else:
            print(int(num_1 / num_2))
