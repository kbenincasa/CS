#Creator: Katie Benincasa
#Date: 2/27/23
#Description: This code is a simple magic 8 ball code
#Sources: I did not use any access recourse as I already knew how to use the random commands
#Bugs: if intergers are inputted instead of words, the code will have an error

import random # imports the random library as I need to use its functions
while True: # creates a constant loop of the code below until broken
    yo = input("What would you like to know? ")#assigns variable "yo" to the users answer to the questions in quotes
    if (yo[-1] == "?" or yo.lower() == "stop"):#this line of code creates an if statement that runs the code below checks to see if the answer has a ? at the end or is stop
       if (yo.lower() == "stop"): # if the answer to the questions is stop, upper or lower case, the below code runs
            break # the while loop is broken
       answer = ["maybe", "yes", "no", "ask again later"] # the list of answers that can respond to the user
       reply = random.choice(answer) # assigns variable "reply" equal to one of the four answers in the list
       print(reply) # prints the variable "reply" to the user
    else: #the code below runs if the above criteria is not met
        print("Please enter a question with a question mark to end or stop")#prints what is in quotations
    
