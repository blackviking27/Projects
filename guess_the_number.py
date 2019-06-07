# importing random module to generate a random number
from random import *
print("Welcome to guess a number")
i = 0
try:
    while i >= 0:
        nums = randint(1,6)   # genrating random number with "randint" function
        a=int(input("Guess a number between 1 and 6"))
        if a!=nums:         # checking if the user has guessed correctly or not
            print("You were close by",(nums-a))
        else:
            break
        i += 1
    print("Finally you have guessed the right number and the number is",a)
    print("Thank you  for playing this game")
except Exception as a:      # all the exceptions are included here
    print("Please enter a number")
    print("The error is",a)

