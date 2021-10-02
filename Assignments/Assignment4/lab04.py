########################################################################
##
## CS 101 Lab
## Program 2
## Anthony Tran
## attnwr@umsystem.edu
##
## PROBLEM : Create a slots machine
##
## ALGORITHM : 
##      1. Ask user how many chips to start with.
##      2. Ask how many chips user wants to wager
##      3. Show 3 random numbers and tell how many matched
##      4. Tell user how many chips they won or lost and tell them their bank
##      5. When user loses, ask if they want to play again
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager less than 0/more than 100
##      play again input. Bank less than 0/more than 100
##
## OTHER COMMENTS:
##      N/A
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play = input('Do you want to play again? ==>')
        play = play.lower()
        if (play == 'y') or (play == 'yes'):
            return True
        elif (play == 'n') or (play == 'no'):
            return False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
        
    return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How many chips do you want to wager? ==>'))
    while (wager < 0) or (wager > bank):
        if wager < 0:
            print('The wager amount must be greater than 0. Please enter again.')
            wager = int(input('How many chips do you want to wager? ==>'))
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
            wager = int(input('How many chips do you want to wager? ==>'))
    return wager            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc):
        matches = 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        matches = 2
    else:
        matches = 0
    return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you want to start with? ==>'))
    while (bank < 0) or (bank > 100):
        if bank < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==>'))
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==>'))
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    #return wager * -1
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 3 - wager
    else:
        return - wager

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spin = 0
        bank_amounts = []
        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            bank_amounts.append(bank)
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spin = spin+1
            

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", sum(bank_amounts), "in", spin, "spins")
        print("The most chips you had was", max(bank_amounts))
        playing = play_again()