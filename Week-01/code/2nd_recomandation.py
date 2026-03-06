# 2nd try at making A small card game recomandation program
# First defining the main function
def main():
# getting user input
    difficulty = input("Difficult or Casual? ").lower()
    players = input("Multiplayer or Single Player").lower()
# Setting conditions
    if not (difficulty == "difficult" or difficulty == "casual"):
        print("Enter a valid difficulty") 
        return
    if not (players == "multiplayer" or players == "single player"):
        print("Enter a valid number of players")
        return    
# Setting conditions
    if difficulty == "difficult" and players == "multiplayer":
        recommend("Poker")
    elif difficulty == "difficult" and players == "single player":
        recommend("Klondik")
    elif difficulty == "casual"and players == "multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")     
# Defining a function that will store the values and print it
def recommend(game):
    print("You might like", game)