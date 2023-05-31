#Author: Katie Benincasa
#Date: 3/8/23
#Description: This program allows the user to play rock paper sizzors against the computer and someone else
#Challenges: This program tells the user who won, their score, allows them to play against someone else, lets them choose their names, reset the score, and finally end the game
#Bugs: So far there are no bugs that I have found
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import random #imports the random library
weapons = ["rock", "paper", "sizzors"]#makes a list called weapons 
cc = random.choice(weapons)#sets variable cc equal to a random choice from the weapons list
score1 = 0#sets the varialbe score1 equal to zero
score2 = 0#sets the variable score2 equal to zero
score = 0#sets variable score equal to 0
def scorep():#makes a function called scorep
    print("Scoreboard:")
    print(p1n,"'s score is:",score1)#prints the score of player one
    print(p2n,"'s score is:", score2)#prints the score of player two
while True:#creates an endless loop
        i = input("What mode would you like? sinlge player or multiplayer?")#sets i equal to input for single or multiplayer
        if (i.lower() == "single player" or i.lower() == "multiplayer"):#creates an if statement so that if the input is not equal to the options the below code runs
            break#breaks the loop
        else:#if above criteria is not me, the code below runs
            print("Please enter 'single player' or 'multiplayer'")#prints what is in quotations
while (i.lower() == "single player"):#creates an endless loop
    if (i.lower() == "single player"):#creates an if statement so that if the player chooses single player the below code runs
        weapon = input("What would you like your weapon to be?")#sets variable weapon equal to the users input 
        while True:#creates an endless loop
            if (weapon.lower() == "rock" or weapon.lower() == "paper" or weapon.lower() == "sizzors"):#creates an if statement so that if weapon is equal to any of the options the below code runs
                break#breaks the endless loop
            else:#if the criteria above is not met, the below code runs
                print("Please enter 'rock', 'paper', or 'sizzors'.")#prints what is in quotations
                weapon = input("What would you like your weapon to be?")#sets the variable weapon equal to a new user input
        weapon = weapon.lower()#sets the variable weapon equal to weapon but all the characters are turned lowercase, altering the string
        if (weapon == "rock"):#creates an if statement so that if weapons is equal to rock the below code runs
                print("The computer chose: " + cc)#prints what is in quotations and the variable cc
                if (cc == "rock"):#creates an if statement looking to see if the computer chose rock
                    print("It was a tie!")#prints what is in quotations
                    print("Your score is: ",score)#prints what is in quotations and the variable score
                if (cc == "paper"):#creates an if statement checking if the computer chose paper
                    print("You lost!")#prints what is in quotations
                    score -= 1#subtracts one from the players score
                    print("Your score is: ",score)#prints what is in quotations and the variable score
                if (cc == "sizzors"):#creates an if statement checking for the input sizzors
                    print("You won!")#prints what is in quotations
                    score += 1#adds one to the player score
                    print("Your score is: ",score)#prints what is in quotations and the variable score
        if (weapon == "paper"):#creates an if statement checkings for the input paper
            print("The computer chose: " + cc)#prints what is in quotations and the variable cc
            if (cc == "rock"):#if statement lookign for rock
                    print("You won!")#prints what is in quotations
                    score += 1#adds one the the player score
                    print("Your score is ",score)#prints what  is in quotations and the variable score
            if (cc == "paper"):#if statement looking for paper
                    print("It is a tie!")#prints what is in quotations
                    print("Your score is ",score)#prints what is in quotations and the variable score
            if (cc == "sizzors"):#if statement looking for input sizzors
                    print("You lost!")#prints what is in quotations
                    score -= 1#subtracts one from the variabls score
                    print("Your score is ",score)#prints what is in quotations and the variable score
        if (weapon == "sizzors"):#if statement looking for sizzors
            print("The computer chose: " + cc)#prints what is in quotations and the variable cc
            if (cc == "rock"):#if statement looking for rock
                    print("You lost!")#prints what is in quotations
                    score -= 1#subtracts one from the variable score
                    print("Your score is ", score)#prints what is in quotations and the variable score
            if (cc == "paper"):#if statements looking for the input paper
                    print("You won!'")#prints what is in quotations
                    score += 1#adds one to the variable score
                    print("Your score is ", score)#prints what is in quotations
            if (cc == "sizzors"):#if statement looking for sizzors
                    print("It was a tie!'")#prints what is in quotations
                    print("Your score is: ", score)#prints what is in quotations and the variable score
        reset = input("Would you like to reset? reply with yes or no")#sets variable reset equal to user input
        reset = reset.lower()#sets variable reset equal to reset with all lowercase characters
        if (reset == "yes"):#if statement checking for user input
            score = 0#sets the variable score1 equal to zero
        end = input("would you like to stop? reply with yes or no")#sets variable end equal to user input
        end = end.lower()#sets variable end equal to end with all lowercase characters
        if (end == "yes"):#if statement checking for user input
            break#breaks the while loop break
while (i.lower() == "multiplayer"):
    p1n = input("What is your name Player one?")#sets variable p1n equal to user input
    p2n = input("What is your name Player two?")#sets variable p2n equal to user input
    while True:#creates an endless loop
        if (i.lower() == "multiplayer"):#if statement looking for the input 'multiplayer'
            p1 = input("What would you like your weapon to be, " + p1n + "?")#sets variable p1 equal to user input
            p1 = p1.lower()#sets p1 equal to p1 with all lowercase characters
            while True:#creates an endless loop
                if (p1 == "rock" or p1 == "paper" or p1 == "sizzors"):#if statement looking for one of three possible inputs
                    break#breaks the loop
                else:#else statement which runs the code below if the 'if' criteria is not met
                    print("Please enter 'rock', 'paper', or 'sizzors'.")#prints what is in quotations
                    p1 = input("What would you like your weapon to be, " + p1n + "?")#sets variable weapon equal to user input
            p2 = input("What would you like your weapon to be, " + p2n + "?")#sets the variable p2 equal to the user input in response to a question
            p2 = p2.lower()#sets variable p2 equal to p2 with all lowercase characters
            while True:#creates an endless loop
                if (p2 == "rock" or p2 == "paper" or p2 == "sizzors"):#if statement checking for user input
                    break#breaks the while loop
                else:#else statement running the code below if criteria above is not met
                    print("Please enter 'rock', 'paper', or 'sizzors'.")#prints what is in quotations
                    p2 = input("What would you like your weapon to be, " + p2n + "?")#sets variable p2 equal to user input
            while True:#creates an endless loop
                if (p1 == "rock"):#if statement checking for user input 
                    if (p2 == "rock"):#if statement checking for user input 
                        print("It was a tie!")#prints what is in quotations
                        scorep()#runs the scorep function defined above
                    if (p2 == "paper"):#if statement checking for user input
                        print(p2n, "won!")#prints p2n and what is in quotations
                        score2 += 1#adds one to variable score2
                        score1 -= 1#subtracts one to varialbe score1
                        scorep()#runs the function scorep
                    if (p2 == "sizzors"):#if statement chekcing for user input
                        print(p1n, "won!")#prints variable p1n and what is in quotations
                        score1 += 1#adds one to variable score1
                        score2 -= 1#subtracts one to variable score2
                        scorep()#runs the functino scorep
                if (p1 == "paper"):#if statement chekcing for user input
                    if (p2 == "paper"):#if statement checking for user input
                        print("It was a tie!")#prints what is in quotations
                        scorep()#runs the function scorep
                    if (p2 == "rock"):#if statement checking for user input
                        print(p1n, "won!")#prints variable p1n and what is in quotations
                        score1 += 1#adds one to the variable score1
                        score2 -= 1#subtracts one to the varialbe score2
                        scorep()#runs the function scorep
                    if (p2 == "sizzors"):#if statement checking for user input
                        print(p2n, "won!")#prints p2n and what is in quotations
                        score1 -= 1#subtracts one to the variable score1
                        score2 += 1#adds one to the varialbe score2
                        scorep()#runs the function scorep
                if (p1 == "sizzors"):#if statement checking for user input
                    if (p2 == "rock"):#if statement checking for user input
                        print(p2n, "won!")#prints variable p2n and what is in quotations
                        score1 -= 1#subtracts one from variable score1
                        score2 += 1#adds one to variable score2
                        scorep()#runs the function scorep
                    if (p2 == "paper"):#if statement checking for user input
                        print(p1n, "won!")#prints variable p1n and prints what is in quotations
                        score2 -= 1#subtracts one from the varialbe score2
                        score1 += 1#adds one to the variable score1
                        scorep()#runs the functino scorep
                    if (p2 == "sizzors"):#if statement checking for user input
                        print("It was a tie!")#prints what is in quotations
                        scorep()#runs the function scorep
                break#breaks the loop
        break
    reset = input("Would you like to reset? reply with yes or no")#sets variable reset equal to user input
    reset = reset.lower()#sets variable reset equal to reset with all lowercase characters
    if (reset == "yes"):#if statement checking for user input
        score1 = 0#sets the variable score1 equal to zero
        score2 = 0#sets the variable score2 equal to zero
    end = input("would you like to stop? reply with yes or no")#sets variable end equal to user input
    end = end.lower()#sets variable end equal to end with all lowercase characters
    if (end == "yes"):#if statement checking for user input
        break#breaks the while loop
            

