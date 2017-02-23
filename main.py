#!/usr/bin/env python
import sys
import random

while True:
    randChoice = str(random.randint(0,2))
    userChoice = raw_input('Enter 0 for rock, 1 for paper and 2 for scissors. Enter "q" to quit\n')
    print(userChoice)
    print(randChoice)

    if str(userChoice) in ['1','2','3','q']:
        if str(userchoice) == 'q':
            sys.exit('Goodbye!')
        if str(userChoice) == randChoice:
            print "Tie"
        elif userChoice == "0" and randChoice == "2":
            print "You Win"
        elif userChoice == "1" and randChoice == "0":
            print "You Win"
        elif userChoice == "2" and randChoice == "1":
            print "You Win"
        else:
            print "You Lose"
    else:
        print('invalid input')
