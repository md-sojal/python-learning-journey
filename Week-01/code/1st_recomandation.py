# 1st try at making A small card game recomandation program
# First defining the main function
def main():
# getting user input
    difficulty = input("Difficult or Casual? ").lower()
    players = input("Multiplayer or Single Player").lower()
# Setting conditions
    if difficulty == "difficult":
        if players == "multiplayer":
            recommend("Poker")
        elif players == "single player":
            recommend("Klondik")
        else:
            print("Enter a valid number of players")
    elif difficulty == "casual":
        if players == "multiplayer":
            recommend("Hearts")
        elif players == "single player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")        
    else:
        print("Enter a valid difficulty")        
# Definging a function that will store the values and print it
def recommend(game):
    print("You might like", game)