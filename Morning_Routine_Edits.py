# Katie Benincasa - 10/11/22 - Morning Routine Program - Only use numbers for the quesiton about time or else it will end the code - I used while loops and functions to allow for more inputs and a seperate loop for incorrect inputs - 
print("Wake up")
sleep = input("Can I sleep for longer? y/n")
sleep = sleep.lower()    
if sleep == "y" or sleep == "n":
    while sleep == "y":
        if sleep == "y":
            print("Go back to sleep")
            sleep = input("Can I go back to sleep? y/n")
            sleep = sleep.lower()
        if sleep != "y": 
            break
    if sleep == "n":
        print("Brush your teeth")
    else:
        print("Invalid Input. Please respond with y or n to the rest of the questions.")
        print("Brush your teeth")
        byt = input("Are your teeth brushed? y/n")
        byt = byt.lower()
        if byt == "n":
            print("Go brush them")
        elif byt != "n" and byt != "y":
            print("Invalid Input. Brush your teeth and only answer with a y or n.")
    cold = input("Is it cold out? y/n")
    cold = cold.lower()
    if cold == "y":
        print("Put on a sweatshirt then go eat breakfast")
    elif cold != "y" and cold != "n":
        print("Invalid Input. Please answer with a y or n")
    print("Go eat breakfast")
    b = input("Did you eat breakfast? y/n")
    b = b.lower()
    if b == "n":
        print("Eat breakfast")
    elif b != "n" and b != "y":
        print("Invalid Input. Make sure to eat breakfast")
    print("Get in the car")
    time = input("What time is it? Please answer in integers")
    time = int(time)
    if time > 815:
        print("You are late. Get to school and Sign in.")
    else:
        while time != 815:
            if time > 815:
                print("You are late. Hurry to school.")
            else:
                print("It is not time to go yet")
            time = input("What time is it?")
            time = int(time)
            if time == 815:
                break

    car = input("Are you in the car? y/n")
    car = car.lower()
    if car == "y":
            print("Go to school.")
    elif car != "y" and car != "n":
        print("Invalid Input. Get in the car and go to school.")
    else:
        print("Get in the car and go.")
else:
    print("Invalid Input. Please answer with a y or n.")
    r = input("Would you like to restart? y/n")
    r = r.lower()
    if r == "y":
        print("Please restart this program and try again.")
    else:
        print("Goodbye")
