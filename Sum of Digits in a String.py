#Sabrina Turney
#October 29, 2018
#Sum of Digits in a String
#This program takes a single string value from the user in the form of digits
#without any spaces. It then converts each digit from the string, adds them,
#and returns the value to the user.


#Intro module explains program to user and looks professional.
def intro():
    print('Welcome to the Sum of Digits calculator!')
    print('\nFirst, enter a number of digits without any spaces.')
    print('Then this program will split up all those digits, add them,')
    print('and then return the value of all the digits to you!')
    #I make a lot of use of newlines to separate the info for the user.
    
    #Adding a bit of clarification for the end user.
    print('\nYour input should look something like this: "12345",')
    print('and the program will do the rest!')
    
#Our main module here brings it all together.
def main():
    #Declare variables to be used
    userString = ''
    #As instructed in the lab, the number will start as a string.
    myList = []
    totalSum = 0
    #I'll be using an array to add the digits together.

    #Call our introduction module
    intro()
    
    #Our calculations take place here:
    #A simple input converted to string and repeated back to them:
    #I add a separation here, plus newlines to make things clear.
    print('----------------------------------------------------')
    userString = str(input('Please enter your single digit list now: '))
    print('You\'ve entered the number \n' + userString + '!')

    #I create a list that separates each digit in the user's input
    #Then call it a new variable once I add all the digits.
    myList = [int(digit) for digit in (userString)]
    totalSum = sum(myList)
    #Here's our final number we need to display to the user.
    
    #We call a "goodbye" module to wrap up the program.
    outro(userString, totalSum)
    
def outro(userString, totalSum):
    #For an outro, the program repeats the number the user entered,
    #then displays their "total digit value"--And thanks them for using it!
    print('\nFor the number your entered, ', userString)
    print('The total value of the digits are: ', totalSum)
    print('Thank you for using my program! Goodbye!')

main()
#Call the main function for the user.
