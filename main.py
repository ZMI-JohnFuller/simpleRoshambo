#!/usr/bin/env python
import sys
import random


options = ['1', '2', '3', 'q']
wins = 0

def process_player_turn():
    choice = input("Enter 1 for Rock, 2 for Paper and 3 For Scissors. To quit, enter 'q'\n")
    if choice.lower() in options:
        if choice == '1':
            print("You chose ROCK")
            return 'rock'
        elif choice == '2':
            print("You chose PAPER")
            return 'paper'
        elif choice == '3':
            print("You chose SCISSORS")
            return "scissors"
        elif choice == 'q':
            sys.exit("Game Over!")
    else:
        return "Invalid choice"


def process_cpu_turn():
    choice = str(random.randint(1,3))
    if choice == '1':
        print("The Computer chooses ROCK")
        return 'rock'
    elif choice == '2':
        print("The Computer chooses PAPER")
        return 'paper'
    elif choice == '3':
        print("The Computer chooses SCISSORS")
        return "scissors"
    else:
        return "Invalid choice"


def roshambo():
    global wins
    wins = 0
    userChoice = process_player_turn()

    if str(userChoice).lower() == 'q':
        sys.exit("Game Over!\nYou have won {} games!".format(wins))
    else:

        computerChoice = process_cpu_turn()

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
