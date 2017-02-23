#!/usr/bin/env python

import sys
import random

while True:
    randChoice = random.randint(0,2)
    userChoice = input('Enter 1 for rock, 2 for paper and 3 for scissors. Enter "q" to quit\n')
    print(userChoice)
    print(randChoice)
    if userChoice in ['1','2','3','q']:
        if userChoice == 'q':
            sys.exit('Goodbye!')
        if userChoice == '1':
            if randChoice == 0:
                print('Tie')
            if randChoice == 1:
                print('Lose')
            if randChoice == 2:
                print('Win')
        if userChoice == '2':
            if randChoice == 0:
                print('Win!')
            if randChoice == 1:
                print('Tie')
            if randChoice == 2:
                print('Lose')
        if userChoice == '3':
            if randChoice == 0:
                print('Lose')
            if randChoice == 1:
                print('Win!')
            if randChoice == 2:
                print('Tie')

    else:
        print('invalid input')
