########################################################################
##
## CS 101 Lab
## Program 2
## Anthony Tran
## attnwr@umsystem.edu
##
## PROBLEM : Find the user's number using only the remainders when
##           divided by 3, 5, 7.
##
## ALGORITHM : 
##      1. Taking remainders of the user's number
##      2. Check them with every number 1-100
##      3. Find the user's number
##      4. Ask if the user wants to play again
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##      If the user inputs a remainder not in the range of a correct remainder,
##      it tells the user teh range of the correct remainder
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

print('Welcome to the Flarsheim Guesser!\n')
replay = 'Y'
#This is the beginning of the loop.
while replay == 'Y':
    print('Please think of a number between and including 1 and 100.\n')
    #This is where the user inputs their remainders
    remainder_3 = int(input('What is the remainder when your number is divided by 3?'))
    #This loop is so the user doesn't input a wrong remainders outside of the boundaries
    while(remainder_3 < 0) or (remainder_3 > 3):
        if remainder_3 <0:
            print('The value entered must be 0 or greater')
            remainder_3 = int(input('What is the remainder when your number is divided by 3?'))
        elif remainder_3 >= 3:
            print('The value entered must be less than 3')
            remainder_3 = int(input('What is the remainder when your number is divided by 3?'))
    print()
    remainder_5 = int(input('What is the remainder when your number is divided by 5?'))
    while(remainder_5 < 0) or (remainder_5 > 5):
        if remainder_5 <0:
            print('The value entered must be 0 or greater')
            remainder_5 = int(input('What is the remainder when your number is divided by 5?'))
        elif remainder_5 >= 5:
            print('The value entered must be less than 5')
            remainder_5 = int(input('What is the remainder when your number is divided by 5?'))
    print()
    remainder_7 = int(input('What is the remainder when your number is divided by 7?'))
    while(remainder_7 < 0) or (remainder_7 > 7):
        if remainder_7 <0:
            print('The value entered must be 0 or greater')
            remainder_7 = int(input('What is the remainder when your number is divided by 7?'))
        elif remainder_7 >= 7:
            print('The value entered must be less than 7')
            remainder_7 = int(input('What is the remainder when your number is divided by 7?'))
    print()
    #This loop calculates the remainders and finds the number the user is thinking of
    for answer in range(1,101):
        if (answer % 3) == remainder_3:
            if (answer % 5) == remainder_5:
                if (answer % 7) == remainder_7:
                    print('You number was', answer)
                    print('Amazing is that?\n')
    #This is the loop where the user can choose to play again or not
    replay = input('Do you want to play again? Y to continue, N to quit  ==>')  
    while (replay != 'Y'):
        if replay == 'N':
            break
        else:
            replay = input('Do you want to play again? Y to continue, N to quit  ==>')
    if replay == 'Y':
        continue
