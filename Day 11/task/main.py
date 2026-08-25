import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

new_game = True

# functions !--------------
def total_score_in_hand(hand):
    score = 0
    for f in hand:
        score += f
    return score

def total_score_with_ace_count(hand):
    if total_score_in_hand(hand) > 21:
        for f in range(0, len(hand)):
            if hand[f] == 11:
                hand[f] = 1
        return total_score_in_hand(hand)
    else:
        return total_score_in_hand(hand)

def plus_one_card(hand):
    hand += [cards[random.randint(0, len(cards) -1)]]
#   return hand

# START OF GAME -------------------
while new_game == True:
    player_hand = []
    cpu_hand = []
    do_we_start = input("Do you want to play a game of Blackjack? Type 'y or 'n':   ").lower()
    start_a_round = True

    if do_we_start == "y" or do_we_start == "yes":
        plus_one_card(player_hand)
        plus_one_card(cpu_hand)

        while start_a_round:
            plus_one_card(player_hand)
            if total_score_with_ace_count(player_hand) > 21:
                print("You went over. You lose... 🤦‍♀️")
            else:
                print(f"    Your cards :{player_hand}, current score: {total_score_in_hand(player_hand)}")

                plus_one_card(cpu_hand)
                print(f"    Computer's first card: {cpu_hand[0]}")
                another_card = input("Type 'y' to get another card, type 'n' to pass:   ").lower()

            if another_card == 'y' or another_card == 'yes':
                #Let's do another one
                start_a_round = True
            elif another_card =='n' or another_card == 'no':
                start_a_round = False
            else:
                print("Wrong input..?")

        while total_score_with_ace_count(cpu_hand) <= 16:
            plus_one_card(cpu_hand)
            total_score_with_ace_count(cpu_hand)



# FINAL HANDS______________
        print(f"    Your final hand: {player_hand}, final score: {total_score_in_hand(player_hand)}")
        print(f"    Computer's final hand: {cpu_hand}, final score: {total_score_in_hand(cpu_hand)}")

        if total_score_in_hand(player_hand) == total_score_in_hand(cpu_hand):
            print("It's a Draw !")
        elif total_score_with_ace_count(player_hand) > 21:
    #        if total_score_in_hand(player_hand):
            print("You went over. You lose... 🤦‍♀️")
        elif total_score_with_ace_count(cpu_hand) > 21:
      #      if total_score_in_hand(cpu_hand):
            print("Opponent went over. You win ! 🦄")
        elif total_score_with_ace_count(player_hand) > total_score_with_ace_count(cpu_hand):
            print("You won ! 🎉")
        elif total_score_with_ace_count(cpu_hand) > total_score_with_ace_count(player_hand):
            print("You lose... 🤢")
        else:
            print("Error..?")
    elif do_we_start == "n" or do_we_start == "no":
        new_game = False
        start_a_round = False
    else:
        print("Wrong input")