# IMPORT ANOTHER PAGE
# RANDOMS
import random

"""import my_module
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_fav_number)"""

"""random_numb_0_to_1 = random.random() * 10
print(random_numb_0_to_1)"""

"""random_float = random.uniform(1, 10)
print(random_float)"""

coin_toss = random.randint(1,2)

if coin_toss == 1:
    print("Heads")
elif coin_toss == 2:
    print("Tails")
else:
    print("Something's wrong")