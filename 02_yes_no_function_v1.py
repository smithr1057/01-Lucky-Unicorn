

# Functions go here...
def yes_no(question):
    while True:
        response = input(question).lower()
        print()

        if response == "yes" or response == "y":
            response = "yes"
            return  response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(" **ERROR** please enter either yes / no")
            print()


# Main Routine goes here...
show_instructions = yes_no("Have you played the game before? ")

print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you have fun? ")
print(" You said {} to having fun".format(having_fun))





