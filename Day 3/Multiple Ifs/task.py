print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
photo_price = int()

if height >= 120:
    photo_yes_no = str(input("You can ride the rollercoaster,\ndo you want the picture included? \n Yes / No ?\n"))
    if photo_yes_no == "Yes":
        photo_price = 3
    else:
        photo_price = 0

    age = int(input("What is your age? "))

    if age <= 12:
        print(f"Please pay ${5 + photo_price}.")
    elif age <= 18:
        print(f"Please pay ${7 + photo_price}.")
    else:
        print(f"Please pay ${12 + photo_price}.")

else:
    print("Sorry you have to be taller to ride.")
