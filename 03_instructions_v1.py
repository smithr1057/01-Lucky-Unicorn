

# Functions go here...
def yes_no(question):
    while True:
        response = input(question).lower()
        print()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(" **ERROR** please enter either yes / no")
            print()


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")


if played_before == "no":
    instructions()

print("Program Continues")