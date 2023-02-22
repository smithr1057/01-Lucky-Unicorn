# Functions go here
def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

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


# Main routine goes here
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
