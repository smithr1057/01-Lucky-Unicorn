import random

# main routine goes here
tokens = ["unicorn", "horse", "horse", "horse", "donkey", "donkey", "donkey", "zebra", "zebra", "zebra", ]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 500):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= .5

# Output
print()
print(f"Starting Balance: ${STARTING_BALANCE:.2f}")
print(f"Final Balance: ${balance:.2f}")

