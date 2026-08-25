# Les deux sont bons mais le 2 est beaucoup plus court

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

banker_roulette = random.randint(0, len(friends) -1)

print(friends[banker_roulette])
print(banker_roulette)

# --------------------------
# Simple as fuck
print(random.choice(friends))
