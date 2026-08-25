print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

# 12ans = 5 / 18 = 7 / + = 12

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("plz 5€")
    elif age <= 18:
        print("plz 7€")
    else:
        print("12€ plz")
else:
    print("Sorry you have to be taller to take this ride.")
