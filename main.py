#!/usr/bin/env python
import sys
import random


options = ['1', '2', '3', 'q']
wins = 0


def process_turn(player):
    if player == "cpu":
        choice = str(random.randint(1,3))
    else:
        choice = input("Enter 1 for Rock, 2 for Paper and 3 For Scissors. To quit, enter 'q'\n>> ")

    if choice.lower() in options:
        if choice == '1':
            if player == 'cpu':
                print("The Computer chooses ROCK")
            else:
                print("You chose ROCK")
            return "rock"
        if choice == '2':
            if player == 'cpu':
                print("The Computer chooses PAPER")
            else:
                print("You chose PAPER")
            return "paper"
        if choice == '3':
            if player == 'cpu':
                print("The Computer chooses SCISSORS")
            else:
                print("You chose SCISSORS")
            return "scissors"
        if choice == 'q':
            sys.exit("Game Over!\nYou won {} games!".format(wins))


def roshambo():
    global wins
    userChoice = process_turn("player")

    if str(userChoice).lower() == 'q':
        sys.exit("Game Over!\nYou have won {} games!".format(wins))
    else:

        computerChoice = process_turn("cpu")

        if userChoice == computerChoice:
            print("Tie!")
        elif userChoice == 'rock' and computerChoice == 'scissors' or userChoice == 'scissors' and computerChoice == 'paper' or userChoice == 'paper' and computerChoice == 'rock':
            print("You win!")
            wins = wins + 1
        else:
            print("You lose!")

        return wins


def main():
    choice = 'y'

    while choice.lower() == 'y':
        roshambo()
        choice = input("Play again? (y/n): ")
        if choice.lower() == 'n':
            print("Game Over!\nYou have won {} games!".format(wins))
            break


main()
