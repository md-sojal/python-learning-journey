import random

def main():
    number = random.randint(1, 10)
    tries = int(input("How many tries do you want? "))

    for remaining in range(tries, 0, -1):
        print(f"Tries left: {remaining}")
        guess = int(input("Guess a number (1–10): "))

        if guess == number:
            print("Correct! You won.")
            break
        print("Wrong guess.")

    else:
        print(f"Game over! The number was {number}")

main()