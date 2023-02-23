

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
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
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


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")


if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))