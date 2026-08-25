import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# EASY VERSION = fait

"""password = []
rando = int()"""

"""for f in range(0, nr_letters):
#    print(f"{ letters[random.randint(0, len(letters) -1)]}")
    password += letters[random.randint(0, len(letters) -1)]
#    print(password + "X")
for f in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]
for f in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) -1)]

print(password)"""


# HARD -> réussi mais... chelou
"""for f in range(0,nr_letters):
    password += letters[random.randint(0, len(letters) -1)]
for f in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) -1)]
for f in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) -1)]

for f in range(0, len(password)):
    # send password to db to register it safely
    rando = random.randint(0, len(password) -1)
    print(password[rando])

    password.pop(rando)

print(password)

"""


# Versions corrigées
#EASY

"""password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)"""


#HARD LEVEL

password_list = []

for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for f in password_list:
    password += f

print(f"Your password is : {password}")

