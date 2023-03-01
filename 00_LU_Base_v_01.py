import random

# Functions go here...


#  Checks that user response is yes / no.
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(" **ERROR** please enter either yes / no")
            print()


# Displays instructions <needs editing>
def instructions():
    statement_generator(" How to Play ", "*")
    print()
    print("Choose a starting amount, minimum $1, maximum $10.")
    print("Then press <enter> to play.")
    print()
    return ""


# checks users enter an integer between a low and high number
def num_check(question, low, high):

    error = f"Please enter a whole number between {low} and {high}\n"

    while True:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give error
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Adds decoration to statements that I choose
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")


if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or a zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= .5

    print(f"You got a {chosen}. Your balance is ${balance:.2f}")

    if balance < 1:
        # If balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print()
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
print("Thank you for playing the Lucky Unicorn game")
print(f"*** Your final balance is ${balance} ***")
