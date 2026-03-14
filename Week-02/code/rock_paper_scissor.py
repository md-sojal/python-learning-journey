"""
Workflow
Take user input (rock, paper, scissor)
Computer will choose a option randomly
result print

Logic
rock - rock = tie
rock - paper = paper wins
rock - scissor = rock wins
paper - paper = tie
paper - rock = paper wins
paper - scissor = scissor wins
scissor - rock = rock wins
scissor - paper = scissor wins
scissor - scissor = tie
"""

from random import choice

item_list = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your move: Rock, Paper, Scissors = ").capitalize()

if user_choice not in item_list:
    print("Enter a valid move")
else:
    computer_choice = choice(item_list)

    print(f"Your choice is {user_choice}")
    print(f"Computer choice is {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie")

    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("Rock beats Scissors: YOU WIN")

    elif user_choice == "Paper" and computer_choice == "Rock":
        print("Paper beats Rock: YOU WIN")

    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("Scissors beats Paper: YOU WIN")

    else:
        print("YOU LOSE")