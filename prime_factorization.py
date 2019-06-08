def prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
list =[]
n = int(input("Enter a to find its prime factor"))
for i in range(1,n+1):
    if n % i == 0:
        if prime(i):
            list.append(i)
print("The prime factors of the given numbers is")
for i in list:
    if i != 1:
        print(i)