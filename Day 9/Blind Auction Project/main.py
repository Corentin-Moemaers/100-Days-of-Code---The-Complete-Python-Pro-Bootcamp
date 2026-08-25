# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
# print("\n" * 100)

# it works, no worries
def max_bidder(bidders):
    highest_amount = 0
    winner = ""
    for bid in bidders :
        """print(bid)
        print(highest_amount)
        print(winner)"""
        if int(bidders[bid]) > highest_amount:
            highest_amount = bidders[bid]
            winner = bid
    print(f"The winner of this bid is : {winner} with a bid of {highest_amount}!")


rabbit_is_running = True
bids = {}

while rabbit_is_running:
    # DOESN'T WORK, VALUE GOES IN BEFORE KEY if var[input(key)] = input(value)!!! Must do it the boring way
    # bids[input("What is your name?\n")] =  int(input("How much do you wanna bid?\n"))
    name = input("What is your name?\n")
    bid = int(input("How much do you wanna bid?\n"))
    bids[name] = bid
    another_rabbit = True
    while another_rabbit:
        another_bidder = input("Is there another bidder? y/n\n").lower()
        if another_bidder == "n" or another_bidder == "no":
            rabbit_is_running = False
            another_rabbit = False
            print("\n" * 20)
        elif another_bidder == "y" or another_bidder == "yes":
            another_rabbit = False
            print("\n" * 20)
        else:
            print("Please enter either 'y' or 'n'")

#print(bids)

#max_bidder(bids)

print(f"The winner of this bid is: {max(bids, key=bids.get)} with a bid of {max(bids.values())}!")
