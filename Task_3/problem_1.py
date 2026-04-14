import random

def pick_winner(names):
    if len(names) == 0:
        return "The list is empty!"
    return f"Congratulations {random.choice(names)}!"

print(pick_winner(["Ali", "Mona", "Sara"]))
print(pick_winner(["Omar", "Laila"]))
print(pick_winner([]))
