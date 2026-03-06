Words = {"PAIR": 4, "HAIR":4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("welcome to spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(Words) > 0:
        print(f"{len(Words)} words left!")
        guess = input("Guess a word: ").upper()
        if guess == "GRAPHIC":
            Words.clear()
            print("You've won! ")
        if guess in Words.keys():
            points = Words.pop(guess)
            print(f"Good job! you scored {points} points.")

            
    print("That's the game!")
"""
def main():
    print("Welcome to spelling Bee!")
    for word, points in Words.items():
        print(f"{word} was worth {points} points.")
"""


main()