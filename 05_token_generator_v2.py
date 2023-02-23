import random

# main routine goes here

tokens = ["unicorn", "horse", "zebra", "donkey"]
starting_balance = 100

balance = starting_balance
# Testing loop to generate 20 tokens
for item in range(0, 100):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= .5


print()
print(f"Starting Balance: ${starting_balance}")

