'''
Author: Katie Benincasa
Date: 2/28/24
Description: This code uses a user inputted name and performs various functions with it
Bugs: This code does not have any bugs I have found
Code Tester: Charlie
Log: 2/28/24 - Started mainline
'''

import random       # imported to choose random letters in name

def main():
    ''' 
    function: creates a menu to display available functions and runs accoridly off the users choice
    answer = the users choice of function
    output: the output of the chosen function or an ended program
    '''

    while True:
        name = input("What is your name?")
        print('''Menu: Enter Choice or 'Q' to (Q)uit:"
            1) Get First Name
            2  Get Middle Name(s)
            3) Get Last Name
            4) Get Reversed Name
            5) Get Vowels in Name
            6) Get Constanants in Name
            7) Make Name Lowercase
            8) Make Name Uppercase
            9) Check For Hyphen
            10) Make Name Reversed
            11) Scramble Name
            12) Get Initials
            ''') 
        answer = input("Enter the number of the function")

        if answer == "1":       #assigns functions to numbers that a user can choose from
            print(get_first_name(name))
        elif answer == "2":
            print(get_middle_name(name))
        elif answer == "3":
            print(get_last_name(name))
        elif answer == "4":
            print(get_name_reverse(name))
        elif answer == "5":
            print(get_vowels(name))
        elif answer == "6":
            print(get_constanants(name))
        elif answer == "7":
            print(get_lowercase(name))
        elif answer == "8":
            print(get_uppercase(name))
        elif answer == "9":
            print(get_hyphen(name))
        elif answer == "10":
            print(get_name_reverse(name))
        elif answer == "11":
            print(get_name_scramble(name))
        elif answer == "12":
            print(get_initial(name))
        elif answer == "Q":
            break
        else: 
            print("Error. Try Again")

def get_first_name(name):
    '''
    function: returns the first name of the user
    output: the users first name
    '''
    for i, letter in enumerate(name): #goes through name looking for a space
        if letter == " ":
            return name[:i]

def get_middle_name(name):
    '''
    function: returns the users middle name(s)
    output: the users middle name(s)
    '''
    for i, letter in enumerate(name): #goes through name looking for a space
        if letter == " ":
            a = i
    for i, letter in enumerate(name[::-1]): #goes through name backwards looking for a space
        if letter == " ":
            b = len(name) - i
    return name[b:a]
    

def get_last_name(name):
    '''
    function: returns the users last name
    output: the users last name
    '''
    for i, letter in enumerate(name[::-1]): #goes through name backwards looking for a space
        if letter == " ":
            return name[len(name) - i:]

def get_vowels(name):
    '''
    function: returns the amount of vowels in the users name
    vowel_count = a variable storing the amount of vowels 
    letter_vowel = the vowels in the alphabet
    output: the amount of vowels in a name
    '''
    vowel_count = 0
    letter_vowel = "aeiouyAEIOUY"
    for letter in name:
        for vowels in letter_vowel:
            if letter == vowels:
                vowel_count += 1
    return vowel_count

def get_constanants(name):
    '''
    function: returns the amount of constanants in a name and the frequency
    name = the lowercase name of the user
    constanant_count = dictionary of constanats and how many there are 
    '''
    name = get_lowercase(name)
    constanant_count = {'b':0, 'c':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'m':0,'n':0,'p':0,'q':0,'r':0,'t':0,'v':0,'w':0,'x':0,'z':0}
    for letter in name:
        if letter in constanant_count.keys():
            constanant_count[letter] += 1
    return constanant_count

def get_lowercase(name):
    '''
    function: returns the users lowercase name
    lower_name = an empty list to append letters to
    output: the users lowercase name
    '''
    lower_name = []
    for i in name:
        decimal = ord(i)
        if decimal <= 90 and decimal >= 65:
            lower_name.append(chr(decimal + 32))
        else:
            lower_name.append(i)
    return str(''.join(lower_name))

def get_uppercase(name):
    '''
    function: returns the users uppercase name
    upper_name = an empty list to append letters to
    output: the users uppercase name
    '''
    upper_name = []
    for i in name:
        decimal = ord(i)
        if decimal <= 122 and decimal >= 97:
            upper_name.append(chr(decimal - 32))
        else:
            upper_name.append(i)
    return str(''.join(upper_name))

def get_hyphen(name):
    '''
    function: returns boolean for a hyphen or no hyphen in users name
    hyphen: the variable storing the boolean for the hyphen
    output: True or Flase depending on if there is or is not a hyphen
    '''
    hyphen = False
    for q in name:
        if q == "-":
            hyphen = True
            return True
        else:
            hyphen = False
    
    return hyphen

def get_name_reverse(name):
    '''
    function: returns the users name reversed
    output: users reversed name
    '''
    return name[::-1]

def get_name_scramble(name):
    '''
    function: scrambles the users name and returns it
    scramble: an empty list to add randomized letters to
    name = a list of the users name
    output: the users scrambled name
    '''
    scramble = []
    name = list(name)
    for i in range(len(name)):
        random_letter = random.choice(name)
        scramble.append(random_letter)
        name.remove(str(random_letter))
    scramble = ''.join(scramble)
    
    return scramble

def get_palindrome(name):
    '''
    function: returns boolean if name is a palindrome
    first_name: variable equal to function output of get_first_name
    first_name_reversed: variable equal to function output of get_name_reversed
    output: True or False boolean based on if name is palindrome
    '''
    first_name = get_first_name(name)
    first_name_reversed = get_name_reverse(name)
    if first_name == first_name_reversed:
        return True
    else:
        return False

def get_initial(name):
    '''
    function: returns the initials of the users name
    initial: empty list to appendn initials to
    first_name: variable equal to output of function get_first_name
    middle_name: variable equal to output of function get_middle_name
    last_name: variable equal to output of function get_last_name
    output: users initials
    '''
    initial = []
    first_name = get_first_name(name)
    middle_name = get_middle_name(name)
    last_name = get_last_name(name)
    initial.append(first_name[0])
    initial.append(middle_name[0])
    initial.append(last_name[0])
    return str(''.join(initial))

if __name__ == "__main__":
    main()