#################################
##Brian Hare
##hareb@umkc.edu 
##CS 101 
##Program 4 
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/ 
##  unknown Caesar key. 
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##    
##  Crack(string_text): Decrypts a string by repeatedly calling Decrypt with each 
##    possible key (1 to 25) and remembering the one with a letter frequency 
##    closest to English based on counts of E, T, O, A, I, N. Returns tuple: 
##    decrypted string and decryption key. 
##    
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
################################ 
import string
def Encrypt() -> str:
    '''Caesar-encrypts string using specified key.'''
    result = ''
    string = input('Enter breif text to encrypt: ')
    shift = int(input('Enter the number to shift letters by: '))
    for i in range(len(string)):
        string = string.upper()
        char = string[i]
        result += chr((ord(char) + shift))
    return result



def Decrypt() -> str:
    ''' Decrypts Caesar-encrypted string with specified key. '''
    result = ''
    string = input('Enter breif text to decrypt: ')
    shift = int(input('Enter the number to shift letters by: '))
    for i in range(len(string)):
        string = string.upper()
        char = string[i]
        result += chr((ord(char) - shift))
    return result



def Print_menu():
  '''Prints menu. No user interaction. '''

  print('MAIN MENU:')
  print('1) Encode a string')
  print('2) Decode a string')
  print('Q) Quit')


  
def main(): 
    selection = ''
    while selection != 'Q':
        Print_menu()
        selection = input('Enter your selection=> ')
        if selection == '1':
            print('Encrypted: ', Encrypt())
        if selection == '2':
            print('Decrypted: ', Decrypt())

      
      
# our entire program: 
main() 