def fibb(n): # defining a fibonacci series
    a=0 ; b=1
    i=1
    print(a)
    print(b)
    while i>0:
        c = a+b
        a = b
        b = c
        if c >= n:
            break
        i += 1
        print(c)
n = int(input("Enter a number to which you want to calculate the series"))
fibb(n)     #calling the function with a limit
print("The series end here")
