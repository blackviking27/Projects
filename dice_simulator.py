from random import *
def rannum():
    nums=randint(1,6)
    return nums
i=1
while i>0:
    print(rannum())
    d=input("Do you want to continue Y or N")
    if d == 'N':
        break
    else :
        pass
    i += 1
print("Thank you for using the dice simulator")