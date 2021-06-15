import random
print("\t\t\t\tColor Guessing Game ")
alien_color = ["green", "yellow", "red", "blue"]

chance  = 5
chance_left = 0 
player = 0
computer = 0

while chance_left < chance:
    color = random.choice(alien_color)
    print(color)
    _input = input("Guess the Alien_Color:")
      
    if _input == color:
        player += 1
        print("You Won\n")
        print(f"You have {player} points and computer have {computer}")

    else:
        computer += 1
        print("You Lose!\n")
        print(f"You have {player} points and computer have {computer} points")

    chance_left += 1
    print(f"{chance - chance_left} out of {chance}")

print("Game Over!")

if player == computer:
    print("Tie!")
elif player < computer:
    print("You lose!")
else:
    print("You Win!")
