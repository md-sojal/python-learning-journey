import random

coin = random.choice(["heads", "tails"])

print("Welcome to coin flip")
guess = input("Choose Heads or Tails? ").lower()
if guess == coin:
    print(f"Its {coin} you won")
else:
    print(f"Its {coin} you lost")