#GUESS THE NUMBER GAME.
print("Welcome To Guess The Number Game",)
print("You Have Only 9 Chances", "\n")
v=18
n1 = 0

while(n1<=8):
    n1 = n1+1
    print('Guess a Number')
    a = int(input())
    if a>v:
        print("NOOOOOO")
        print("You Guessed A Smaller Number.")
        print("Remaining", 9-n1, "Chances", '\n')
    elif a<v:
        print("NOOOOOO")
        print("You Guessed A Smaller Number.")
        print("Remaining", 9-n1, "Chances", '\n')
    elif a==18:
        print("CONGRATULATIONS!")
        print("You Guessed the Right Number.")
        break
if 9-n1==3:
    print("HINT: The Number is less then 100")
elif 9-n1==2:
    print("HINT: The Number is not more then 50")
elif 9-n1==1:
    print("HINT: The Number is close to 25")


if 9-n1==0:
    print("GAME OVER")
