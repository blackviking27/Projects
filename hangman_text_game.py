from random_words import * 
# The welcome screen is displayed with the help of this function
def main():
    print("Welcome to Hangman Game")
    print("The rules are simple you have to guess the word")
    print("You are provided limited number of guesses i.e 3")

# checking for a letter that is matching
def check (n,letter):
    temp=0
    for i in range(len(letter)):
        if letter[i] == n:
            l[i] = n
        if letter[i]!=n:
            temp+=1
    if temp == len(letter):
        globals()['guess'] -= 1
# printing the partially guessed word
def show():
    for i in l:
        print(i,end="")
# checking if the word is guessed correctly
def complete():
    temp=0
    for i in range(len(letter)):
        if l[i]==letter[i]:
            temp+=1
    if temp==len(letter):
        return True
    else:
        return False

# generating a random word
r = RandomWords()
letter = r.random_word() # storing a random word in variable
guess = 3 # number of attempts the user has
l = [] # creating a list to check if letter guessed is correct
for i in range(len(letter)):
    l.append('*')

main()
print("The length of the word is ",len(letter))

# executing loop till the user has guesses left
while guess>0:
    n=input("Guess a letter")
    check(n,letter)
    show()
    print()  # starting a new line
    print("The number of guesses left is ",guess)

# now checking if the user guessed the word correctly or not
if(complete()):
    print("You guessed it correctly")
    print('The word is',letter)
else:
    print("Sorry you were not able to guess the word")
    print("The word was",letter)
