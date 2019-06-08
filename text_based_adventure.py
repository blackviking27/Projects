# text based adventure game
print("Welcome to text adventure")
print("You can move in two directions left and right and explore the rooms")
print("but you cannot go beyond the rooms since it is not safe for you as of now")
print("r or right to go in right direction")
print("l or left to go in left direction")
room=[1,2,3,4,5,6]
a = room[0]                 #initial room number
i=1
while i>0:
    try:
            def room(n):                    #defining each room with its own proprties
                print("You are in room number",n)
                if n==1:
                    print("This a magical room full of magic")
                elif n==2:
                    print("This room is full of nightmares all around the world")
                elif n==3:
                    print("This room belongs to the wisest man on the planet")
                elif n==4:
                    print("This room belongs to the strongest man on the planet")
                elif n==5:
                    print("This room belongs to someone unknown for centuries")
                elif n==6:
                    print("This room is out of bounds for people")
            def left():
                l=globals()['a']-1
                if l>=1:
                    room(l)
                else:
                    print("There is no room in that direction")
            def right():
                r =globals()['a']+1
                if r<=6:
                    room(r)
                else :
                    print("There is no room in that direction")
            def main():
                dir = input("Which direction you want to move")
                if dir == 'right' or dir == 'r':
                    right()
                elif dir == 'left' or dir == 'l':
                    left()
                else:
                    print("Enter a valid direction")
            main()
            q=input("If you want to quit you can enter q or exit if not then press enter")
            if q == 'q' or q == "exit":
                break

    except Exception as e:
        pass
    i+=1
print("Thank you for playing the game")
print("Hope to see you again")
