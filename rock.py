import random

values = ['rock','paper','scissors']


def select(x, y):
    print("First player: "+x)
    print("Second player: "+y)
    if x == y:
        print("Equal")
        print("Next round")
        x = random.choice(values)
        y = random.choice(values)
        select(x,y)
    elif x == "rock":
        if y == "scissors":
            print("Rock smashes scissors! First Player win!")
        else:
            print("Paper covers rock! Second Player Win! ")
    elif x == "paper":
        if y == "rock":
            print(" Paper covers rock! First Player win!")
        else:
            print("Scissors cuts paper!Second Player Win!")
    elif x == "scissors":
        if y == "paper":
            print("Scissors cuts paper! First Player Win!")
        else:
            print(" Rock smashes scissors! Second Player Win")

x = random.choice(values)
y = random.choice(values)
select(x,y)
