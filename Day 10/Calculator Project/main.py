import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

all_functions = {
    "+": add
    ,"-": subtract
    ,"*": multiply
    ,"/": divide
}
rabbit_is_running = True

#print(all_functions["*"](4, 8))
while rabbit_is_running :
    print(art.logo)
    chosen_n1 = float(input("What's the first number?:    "))
    rabbit_n2_is_jumping = True

    while rabbit_n2_is_jumping:
        for f in all_functions:
            print(f)
        chosen_operation = input("Pick an operation:    ")
        chosen_n2 = float(input("What's the next number?:    "))
        output = all_functions[chosen_operation](chosen_n1, chosen_n2)
        print(f"{chosen_n1} {chosen_operation} {chosen_n2} = {output}")
        continue_calculations_or_reset = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation:    ").lower()

        if continue_calculations_or_reset == "y" or continue_calculations_or_reset == "yes":
            chosen_n1 = output
        elif continue_calculations_or_reset == "n" or continue_calculations_or_reset == "no":
            print("\n * 20")
            rabbit_n2_is_jumping = False
        else:
            print("Wrong input, please redo the calculation.")
            rabbit_n2_is_jumping = False
