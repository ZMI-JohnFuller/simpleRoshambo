#!/usr/bin/env python
import sys

def getInput():
    userInput = input('Please enter your choice:\nRock, Paper or Scissors? (Type "Quit" to exit)\n')
    print(userInput)
    validateInput(userInput)
    print(userInput)

def validateInput(userInput):
    print ('validating input...')
    if userInput:
        if userInput.lower() not in ['rock', 'paper', 'scissors']:
                print('Nope!')
        elif userInput is '':
            print('Invalid input')
        elif userInput.lower() in 'quit':
            sys.exit(2)
        elif userInput.lower() in ['rock','r']:
            print ('you chose rock')
    else:
        print('stop messing up')
def main():
    while True:
        getInput()

main()
