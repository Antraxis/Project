import string
import keyword
one= input("enter")
one_1=one.split()
if not one.islower() or one[0].isdigit():
    print('False1')
else:
    for one_0 in one:
        if one_0 in string.punctuation or one_0== " ":
            print("False2")
            break
    else:
        for one_2 in one_1:
            if one_2 in keyword.kwlist:
                print("False3")
                break
        else:
            print(True)