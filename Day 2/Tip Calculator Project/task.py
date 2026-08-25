print("Welcome to the tip calculator! \n")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15 \n"))
people = int(input("How many people to split the bill? \n"))
total = bill * (tip / 100 + 1) / people
# or total = round(bill * (tip / 100 +1) / people
# so last print -> {total} instead of {round(total, 2)}


print(f"Each person should pay : {round(total, 2)}")

