#!/usr/bin/env python
global userInput

def getInput(userInput):
    userInput == input('Please enter your choice:\nRock, Paper or Scissors? (Type "Quit" to exit)\n')
    validateInput(userInput)

def validateInput(userInput):
    print ('validating input...')
    if userInput == '':
        return print('Invalid input')
    if userInput == 'Quit':
        exit()
    else:
        print('You chose "' + userInput + '" ')

def inputHandler(userInput):
    getInput(userInput)

def main():
    while True:
        inputHandler(userInput)
main()
