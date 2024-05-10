'''
Author: Katie Benincasa
Date: 4/2/23
Description: Creates a game of Battleship against a computer
Imports: - random for randomizing coordinates on the computers board
Bugs: This code does not have any bugs I have found
Log: 4/2/2023 - Started mainline
'''
from random import randint

def main():
    '''
    Function: menu to run the functions within the code
    c_array: the array of the computers battle board
    p_array: the array of the players battle board
    output: the functions for battle ship
    '''
    c_array = [["🌊" for i in range(5)] for j in range(5)]
    p_array = [["🌊" for i in range(5)] for j in range(5)]

    computer(c_array)
    player(p_array)
    play(c_array, p_array)

def player(p_array):
    '''
    Function: sets up the players board with ships and has try except for out of bounds coordinates
    Q: random variable to store number of times to loop code
    x_user: the variable storing the 'x' coordinate for the user's ship
    y_user: the variable storing the 'y' coordinate for the user's ship
    output: either the array with ships now placed or an out of bounds message
    '''
    Q = 4

    while Q > 0:
        try:
            x_user = int(input("what would you like your ship's x corrdinate to be. 1-5")) - 1
            y_user = int(input("what would you like your ship's y coordinate to be. 1-5")) - 1
            print()
            while p_array[y_user][x_user] == "🚢":
                print("Coordinate already chosen. Please pick a new one.")
                x_user = int(input("what would you like your ship's x coordinate to be. 1-5")) - 1
                y_user = int(input("what would you like your ship's y coordinate to be. 1-5")) - 1
                print()
            p_array[y_user][x_user] = 1
            Q -= 1
        except:
            print("Out of Bounds. Please enter a valid coordinate.")

def computer(c_array):
    '''
    Function: places four random ships on the computers board
    z: random variable storing number of times to loop code
    x_comp: the randomized 'x' cooridante of the computer's ship
    y_comp: the randomized 'y' cooridante of the computer's ship
    output: the computer's board with ships on it
    '''
    z = 0

    while z < 4:
        x_comp = randint(0,4)
        y_comp = randint(0,4)
        if c_array[x_comp][y_comp] != 1:
            c_array[x_comp][y_comp] = 1
            z += 1
    return c_array

def play(c_array, p_array):
    '''
    Function: using both the computers and players board, it alternates turns shooting the boards and prints them with emojis
    tries: the number of times the player and computer can shoot
    num_ships_player: the number of ships the user hit
    num_ships_com: the number of ships the computer hit
    output: the boards of the computer and player and the result of the game
    '''
    tries = 10
    num_ships_player = 0
    num_ships_com = 0

    while tries > 0:
        try:
            x_user = int(input("What x-coordinate would you like to hit?")) - 1
            y_user = int(input("What y-coordinate would you like to hit?")) - 1
            while c_array[y_user][x_user] == "🚢" or c_array[y_user][x_user] == "💣":
                print("Coordinate already chosen. Please pick a new one.")
                x_user = int(input("What x-coordinate would you like to hit?")) - 1
                y_user = int(input("What y-coordinate would you like to hit?")) - 1
                if c_array[y_user][x_user] == "🚢" or c_array[y_user][x_user] == "🌊":
                    break
            if c_array[y_user][x_user] == 1:
                    print("You hit a ship!")
                    c_array[y_user][x_user] = "🚢"
                    num_ships_player += 1
                    tries -= 1
                    print("You have:",tries,"turns left.")
            else:
                print("You missed.")
                c_array[y_user][x_user] = "💣"
                tries -= 1
                print("You have:",tries,"turns left.")
            print("Here is your board:")
            for i in c_array:
                print(' '.join([b if b != 1 else "🌊" for b in i])) #printing the players board without brackets and commas and if the cooridante is equal to one it prints a water emoji
            x_com = randint(0,4)
            y_com = randint(0,4)
            print("The computer chose: (",x_com + 1,",",y_com + 1,")")
            if p_array[y_com][x_com] == 1:
                print("The computer hit one of your ships")
                p_array[y_com][x_com] = "💥"
                num_ships_com += 1              
            else:
                print("The computer missed.")
                p_array[y_com][x_com] = "💣"
            print("Here is the computer's board:")
            for i in p_array:
                print(' '.join([b if b != 1 else "🌊" for b in i])) #printing the computers board without brackets and commas and if the cooridante is equal to one it prints a water emoji
            if num_ships_player == 4 or num_ships_com == 4:
                break
        except:
            print("Out of Bounds. Please enter a valid coordinate.")
            
    if num_ships_player < num_ships_com:
        print("You lost.")
        print("The score was:",num_ships_player,"/4 you to",num_ships_com,"/4 computer")
    elif num_ships_com == num_ships_player:
        print("You tied.")
        print("The score was:",num_ships_player,"/4 you to",num_ships_com,"/4 computer")
    else:
        print("You won!")
        print("The score was:",num_ships_player,"/4 you to",num_ships_com,"/4 computer")
    
if __name__ == '__main__':
    main()
