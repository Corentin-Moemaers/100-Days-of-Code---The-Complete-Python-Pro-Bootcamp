# Rock Paper Scissors / MODIFIED --> .index() et len()

import random

rock = ["Rock",
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''']

paper = ["Paper",
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''']

scissors = ["Scissors",
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

# Didn't wanna just hard-write the rules in there...
"""(
       player_choice == rock_paper_scissors[0] and cpu_choice == rock_paper_scissors[1]
       or player_choice == rock_paper_scissors[1] and cpu_choice == rock_paper_scissors[2]
       or player_choice == rock_paper_scissors[2] and cpu_choice == rock_paper_scissors[3]
       ):"""

rock_paper_scissors = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_choice = rock_paper_scissors[random.randint(0,2)]

# print(rock_paper_scissors.index(player_choice) +1)

if  player_input < len(rock_paper_scissors) and player_input >= 0:
    player_choice = rock_paper_scissors[player_input]
    print("You chose :", *player_choice, "\n")
    print("Computer chose :", *cpu_choice)
    if player_choice == cpu_choice :
        print("It's a Draw!")
    elif rock_paper_scissors.index(cpu_choice) == (rock_paper_scissors.index(player_choice) +1 ) % 3 :
        print("You lost.")
    else:
        print("You win!")
else:
    print("You didn't chose a correct number, You lose!")
