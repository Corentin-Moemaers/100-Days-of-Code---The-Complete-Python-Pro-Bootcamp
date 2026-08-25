from asyncio import print_call_graph

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You enter a castle in hope of finding a treasure, you walk a bit and encounter an intersection")
print("Do you go left or right?")
turn_one = input("Left / Right")

if turn_one.lower() == "right":
    print("You entered a big room where trolls were sleeping...")
    print("You woke them up...")
    print("Game Over")
elif turn_one.lower()  == "left":
    print("You entered an indoor swimming pool")
    print("An orc is splashing around like a Magikarp")
    print("He doesn't seem that dangerous...")
    print("Do you wait or do you swim trough?")
    turn_two = input("Wait / Swim")
    if turn_two.lower() == "swim":
        print("The orc instantly turn it's head and look right into your soul")
        print("It's eyes are two burning rubies from hell")
        print("You feel it in your bones,")
        print("you're f#cked...")
        print("Game Over")
    elif turn_two.lower() == "wait":
        print("The orc stopped splashing around...")
        print("You wait...")
        print("You see one or two bubbles poping at the surface of the water")
        print("...")
        print("The bubbles stopped appearing for a while now...")
        print("Did it drowned..?")
        print("You silently pray for it and continue your way in, leaving the room with lots of questions...")
        print("You seem to get into another intersection")
        print("This time there are 3 doors")
        print("On the left is a Blue door,")
        print("ahead of you is a Yellow one,")
        print("on your right is a Red one.")
        print("Wich one do you open?")
        turn_three = input("Blue / Yellow / Red?")
        if turn_three.lower() == "blue":
            print("You open the blue door and hear a *Snap!*")
            print("Why is my body over there, upside down?")
            print("Your vision fade to black, you'll never know what hit you...")
            print("Game Over")
        elif turn_three.lower() == "red":
            print("The red door creak when opened...")
            print("*STACK!*")
            print("You just received an arrow in your right shoulder!")
            print("You try to endure the pain and feel that there was a poison on this arrow...")
            print("Wait... it's not an arrow... and...")
            print("Why is everything...")
            print("You see a glimpse of a horrible looking, full of boils, dirty... woman?")
            print("Maybe...")
            print("She comes at you with a gilly smile.")
            print("Your vision becomes blurry...")
            print("But it becomes clear all of a sudden, you've regained strenght and are ready to fight!")
            print("You look at the abomination and...")
            print("Mom...?")
            print("*Yes darling* she says, *you're apparently fucked up for loving your mom that much...*")
            print("*Well, no biggies, you're mine now!")
            print("*Come give a BIG 'Hug' to Mama!")
            print("... The poison was a love serum")
            print("You can't resist the urge of your true love")
            print("And even if you're still in there, knowing that it's just a filthy... thing...")
            print("You're still enjoying every moments with that thing,")
            print("even reduced as the state of a brainless slave.")
            print("Game Over")
        elif turn_three.lower() == "red":
            print("You found the treasure yoohoo banzaï")
            print("I must go take a shower I'm tired")
            print("You Win!")
            print("Yay...")
        else:
            print("Wrong input sorry, back to the beginning !")
    else:
        print("wrong input sorry, back to the beginning!")
else:
    print("wrong input sorry, back to the beginning I guess?")