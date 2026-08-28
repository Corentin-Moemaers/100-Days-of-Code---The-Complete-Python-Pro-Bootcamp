import art
import random
import game_data

#vars
DATA = game_data.data
data_a = {}
data_b = {}

# def compare(a, b)
def compare(a, b):
    score = 0
    die = False

    while not die:
    # print art
        print(art.logo)

        # Display user's score
        if score > 0:
            print(f"You're right ! Current score: {score}.")

        if a == {}:
            a = random.choice(DATA)

    # print A
        print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")

    # print VS art
        print(art.vs)

    # print B
        b = random.choice(DATA)
    # no DRAWS allowed
        while b == a:
            b = random.choice(DATA)

        print(f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}")

    # User choice + check if win or lose
        answer = True
        while answer:
            choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
            if choice == "a" or choice == "b":
                answer = False

                if a.get("follower_count") > b.get("follower_count"):
                    if choice == "a":
                        score += 1
                        a = b
                    else:
                        print(f"Sorry, that's wrong. Final score: {score}")
                        return

                elif a.get("follower_count") < b.get("follower_count"):
                    if choice == "b":
                        score += 1
                        a = b
                    else:
                        print(f"Sorry, that's wrong. Final score: {score}")
                        return
            else:
                print("Wrong input, please try again.")

compare(data_a, data_b)
