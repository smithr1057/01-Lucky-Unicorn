# Functions go here


# Main routine goes here

error = "Please enter a whole number between 1 and 10\n"

while True:
    try:
        # Ask the question
        response = int(input("How much would you like to play with? "))

        # if the amount is too low / too high give error
        if 0 < response <= 10:
            print("You Have asked to play with ${}\n".format(response))

        # Output an error
        else:
            print(error)

    except ValueError:
        print(error)
