import math#imports math library
#Creator: Katie Benincasa
#Date: 5/22/23
#Description: This code runs a basic calculator
#Challenges: exponent function, main function, radical function, and user input limiters
#Bugs: none that I have found so far

def add (n, nn):#cretes add function with inputs
    print(n + nn)#prints the added inputs
def sub (n, nn):#creates sub function with inputs
    print(n - nn)#prints the subtracted inputs
def div(n, nn):#creates div function with inputs
    print(n/nn)#prints the divided inputs
def mult (n, nn):#creates mult function with inputs
    print(n*nn)#prints the multiplied inputs
def ex(n,nn):#creates function ex with inputs
    print(n**nn)#prints the expontential input
def ci(n,nn):#creates function ci with inputs
    if n.is_integer():#if statement looking for integer input
        print("The first number is an integer")#prints what is in quotations
    else:#else statement for if the above is not true
        print("The first number is not an integer")#pritns what is in quotations
    if nn.is_integer():#if statement looking for integer input
        print("The second numer is an integer")#prints what is in quotations
    else:#else statement for if the above is not true
        print("The second number is not an integer")#prints what is in quotations
def rad(n):#creates radical function
    print(math.sqrt(n))#prints the square root of variable n
def sum():#creates function sum
    num = input("How many numbers in the list would you like?")#sets variable eual to user input
    num = int(num)#sets variable equal to itself as an integer
    s = 0#sets variable eqaul to zero
    for i in range(num):#for loop running for the range of variable num
        x = input("What number would you like to add?")#sets variable equal to user input
        x = int(x)#sets variable equal to iself as an integer
        s += x#sets variable s equal to itself plus x
    print(s)#prints s    
def main():#creates function main with inputs
    while True:#infinite loop
        print("1: addition. 2: subtraction. 3: division. 4: multiplication. 5: exponents. 6: sum of a list. 7: main. 8: radical. 9: end.")#prints the options for operations
        i = input("What would you like to do? Enter with one of the integer options.")#sets i equal to user input
        while True:#infinite loop
            if i.isnumeric():#if statement checking for numeric user input
                break#breaks the infinite loop
            else:#else statement running if above is not valid
                print("Invalid Input. Please put an integer that is in between 1 and 8")#prints what is in quotations
                i = input("What would you like to do? Enter with one of the integer options.")#sets variable equal to user input
        if i == "9":#if statement checking for user input
            break#breaks while loop
        elif i == "6":#elif lookign for user input
            sum()#calls sum function
        if i == "1":#if statement looking for user input
            n = input("What would you like your first number to be for addition?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your second number to be for addition?")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            add(n,nn)#calls add function
        elif i == "2":#elif statement looking for user input
            n = input("What would you like your first number to be for subtraction?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your second number to be for subtraction")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            sub(n,nn)#calls sub function
        elif i == "3":#elif statement looking for user input
            n = input("What would you like your numerator to be for division?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your denomonator to be for division?")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            div(n,nn)#calls div function
        elif i == "4":#elif statement looking for user input
            n = input("What would you like your first number to be for multiplication?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your second number to be for multiplication?")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            mult(n,nn)#calls mult function
        elif i == "5":#elif statement looking for user input
            n = input("What would you like your base number to be for expontents?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your exponent number to be for exponents")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            ex(n,nn)#calls ex function
        elif i == "7":#elif statement looking for user input
            n = input("What would you like your first number to be for main?")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            nn = input("What would you like your second number to be for main")#sets variable equal to user input
            nn = float(nn)#sets variable equal to itself as a float
            ci(n,nn)#calls ci function
            main(n,nn)#calls main function
        elif i == "8":#elif statement checking for user input
            n = input("What would you like to square root? Please enter a positive number.")#sets variable equal to user input
            n = float(n)#sets variable equal to itself as a float
            rad(n)#calls rad function

main()#calls main function