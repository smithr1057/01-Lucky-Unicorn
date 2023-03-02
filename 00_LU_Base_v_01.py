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
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey, or a unicorn.")
    print()
    print("It costs $1 per round. Depending on your prize you might win some of your money back. Here's the payout "
          "amounts...")
    print("Unicorn: +$4.00")
    print("Horse: -$0.50")
    print("Zebra: -$0.50")
    print("Donkey: -$1")
    print()
    print("Can you avoid the donkeys, and win it big with the unicorns?")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead f pressing <enter>")
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
statement_generator("Welcome to the Lucky Unicorn game", "*")
print()

played_before = yes_no("Have you played the game before? ")
print()


if played_before == "no":
    instructions()

statement_generator("Let's play a game", "-")
print()
# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
print(f"You are playing with ${how_much}")

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
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or a zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= .5

    outcome = f"You got a {chosen}. Your balance is ${balance:.2f}"
    statement_generator(outcome, prize_decoration)

    if balance < 1:
        # If balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print()
        statement_generator("Sorry you have run out of money", "x")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")


print()
statement_generator("Results", "*")
print(f"Final balance ${balance}")
print("Thank you for playing the Lucky Unicorn game")

