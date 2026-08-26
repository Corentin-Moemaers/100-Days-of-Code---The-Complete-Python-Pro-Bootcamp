import random
import art
print(art.logo)

lives = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Number of lives / Difficulty choice
while lives == 0:
    to_find = random.randint(1, 100)
    print(to_find)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else :
        print("Wrong input.")

# Game Start
    game_over = False
    while not game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess\n"))

        if lives == 1 or guess == to_find:
            game_over = True

# Do you wanna play again? Game over
            replaying = False
            while not replaying:
                if guess == to_find:
                    restart_or_not = input("You won! Do you wanna play again? Y/N:\n").lower()
                else:
                    restart_or_not = input(f"You lost... Do you wanna play again? Y/N\n (the answer was {to_find})\n").lower()

                if restart_or_not == "y":
                    lives = 0
                    replaying = True
                elif restart_or_not == "n":
                    lives = -1
                    replaying = True
                else:
                    print("Wrong input.")

# False answer, try again
        elif guess > to_find:
            print("Too high.")
            print("Guess again.")
            lives -= 1
        elif guess < to_find:
            print("Too low.")
            print("Guess again.")
            lives -= 1

# Shouldn't happen but it's to prevent a crash just in case
        else:
            print("Error in part 'Too high/Too low")