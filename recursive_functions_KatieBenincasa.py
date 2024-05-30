'''
Author: Katie Benincasa
Date: 5/22/24
Description: This code takes a user inputted number and performs a series of tasks to it according to the users choice
Log: -Mainline started
Bugs: None have been found
imports: none
'''

def main():
    '''
    Function: Menu for user to navigate available functions based off their inputted number
    number: variable of user's selected number
    choice: variable of user's selected function on their number
    output: the output of the selected function of the user according to their selected number
    '''

    while True:
        number = int(input("Please enter a number"))                                  
        while True:
            choice = int(input("Please choose a function: 0 to quit, 1 for Factorial, 2 for Summation, 3 for Powers, 4 for Sum of Digits, or 5 for Fibonacci: "))     
            if type(choice) == int:
                if -1 < choice < 6:
                    break  

        if choice == 1:                                                       
            print(factorial(number))                                           
        elif choice == 2:
            print(summation(number))
        elif choice == 3:
            exp = int(input("What exponent do you want?"))
            print(powers(number, exp))
        elif choice == 4:
            print(sum_of_digits(number))
        elif choice == 5:
            print(fibonacci(number))
        elif choice == 0:
            break

def factorial(number):
    '''
    Function: multiplies the users number by itself and subtracts 1 until it reaches 0
    number: variable of user's selected number
    output: returns answer to main to be printed
    '''
    
    if number == 1 or number == 0:
        return number
    elif number > 0:
        return number * factorial(number -1)                   

def summation(number):
    '''
    Function: adds the number by itself and subtracts 1 until it reaches 0
    number: variable of user's selected number
    output: returns answer to main to be printed
    '''

    if number == 1 or number == 0:
        return number
    elif number > 0:
        return number + summation(number -1)                    
    
def powers(number, exp):
    '''
    Function: calculates the value of number -1 raised to exp - then multiplies the recursive by exp
    number: variable of user's selected number
    output: returns answer to main to be printed
    '''

    if number > 0:
        return exp * powers(number-1, exp)                    
    elif number == 0:
        return 1
    
def sum_of_digits(number):
    '''
    Function: seperates the last digit of the number and divides the rest by 10 % and then adds the last number back
    number: variable of user's selected number
    output: returns answer to main to be printed
    '''

    if number < 10:
        return number
    else:
        return sum_of_digits(number // 10) + number % 10        
    
def fibonacci(number):
    '''
    Function: adds the number -1 and the number -2 until it becomes 1
    number: variable of user's selected number
    output: returns answer to main to be printed
    '''

    if number == 0 or number == 1:
        return number
    elif number > 1:
        return fibonacci(number -1) + fibonacci(number -2)    
    

if __name__ == '__main__':
    main()