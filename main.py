#!/usr/bin/env python
import sys
import random

while True:
    userChoice = input('Enter 1 for Rock, 2 for Paper and 3 For Scissors. To quit, enter "Q"\n')
    if str(userChoice) in ['1','2','3','q']:
        if str(userChoice) == 'q':
            sys.exit('Goodbye!')
        else:
            #AI conditionals
            randChoice = str(random.randint(1, 3))
            print (randChoice)
            if randChoice == "1":
                print("They chose Rock...")
            if randChoice == "2":
                print("They chose Paper...")
            if randChoice == "3":
                print("They chose Scissors...")

            #user conditionals

            if userChoice == "1":
                print("You chose Rock...")
            if userChoice == "2":
                print("You chose Paper...")
            if userChoice == "3":
                print("You chose Scissors...")

            if str(userChoice) == randChoice:
                print ("Tie")
            elif userChoice == "1" and randChoice == "3" or userChoice == "2" and randChoice == "1" or userChoice =="3" and randChoice =="2":
                print("You win!")
            else:
                print('You lose.')
    else:
        print('Invalid input.\n')
