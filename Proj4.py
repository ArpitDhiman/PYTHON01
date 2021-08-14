#GUESS THE NUMBER GAME.
print("Welcome To Guess The Number Game",)
print("You Have Only 9 Chances", "\n")
v=18
n1 = 0

while(n1<=8):
    n1 = n1+1
    print('Guess a Number')
    a = float(input())
    if a>v:
        print("NOOOOOO")
        print("You Guessed A Larger Number.")
        print("Remaining", 9-n1, "Chances", '\n')
    elif a<v:
        print("NOOOOOO")
        print("You Guessed A Smaller Number.")
        print("Remaining", 9-n1, "Chances", '\n')
    elif a==18:
        print("CONGRATULATIONS!")
        print("You Guessed the Right Number.")
        continue
        
if 9-n1==0:
    print("GAME OVER")
