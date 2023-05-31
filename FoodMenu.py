import random #imports the library random
cook = ["Local", "roasted", "grilled", "garlic mashed", "oven dried", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby", "teriyaki glazed", "steamed"] #creates a list with all of the cook options
main = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "basmati rice", "rainbow carrots", "fingerling potatoes", "three color squash", "potatoes", "eggplant", "drumstick", "short rib", "duck breast", "eye round of beef", "baguette"]#creates a list of the main courses
add = ["with fennel", "gratin", "bengali style with peas", "pizza", "with balsamico", "with garlic and olive oil", "with pigeon peas", "with minted yogurt", "soup", "chutney", "salad", "with tropical fruit salsa", "over sticky rice", "au jus"]#creates a list of the additions
nm = []#creates an empty list for a new menu
ct = [5,6,7,8,5,5.50,9,6,7,8,6,5,9,4]
while True:  #creates an endless loop
    print("How many menu items would you like? Please choose a number under:", (len(main) + 1))#prints what is in quotations as well as the length of the list main + 1
    t = input()#sets variable t equal to user minput
    while True:#creates an endless loop
        if (t.isdigit()):#checks to see if the user input is a digit
                if int(t) < (len(main) +1):#checks if the number entered is less than the length of main + 1 
                    break#breaks the while loop
                else:#this code runs if above is invalid
                    print("Invalid input. Please answer with an integer under:", len(main) + 1)#prints quotations and the lenght of main +1
                    t = input()#sets variable equal to user input
        else:#below code runs if code above is invalid
            print("Invalid input. Please answer with an integer under:", len(main) + 1)#prints quotations and the lenght of main +1
            t = input()#sets variable equal to user input
    t = int(t)#sets variable t to an integer
    i = 0#sets varialbe i equal to 0
    while i < t:#while loop running as long as i is less than t
        cookp = []#creates a new, empty list called cookp
        num = random.randint(1,15)#sets variable num equal to a random number 1-15
        m = random.choice(main)#sets variable m equal to random choice from main
        for x in range(num):#for loop running repeatedly for the value of num
            cookp.append(random.choice(cook))#appends the random choice to cookp list
        a = random.choice(add)
        pf = ct[cookp.index(random.choice(cookp))] + ct[main.index(m)] + ct[add.index(a)]
        print(*cookp, m, a)#prints cookp, m, and a random item from the add list
        print("Price of ↑: $",pf)
        i += 1#sets i equal to i plus one
        main.remove(m)#removes m from the list main
        nm.append(m)#appends m to the list nm
    if len(main) < 1:#if statement looking for length of list main
        print("Thank you for viewing all the menu items. It will now close")#prints what is in quotations
        break#breaks the while loop
    end = input("Would you like to end? yes or no?")#sets end equal to user input
    while True:#creates an endless loop
        if end != "yes" and end != "no":#if statement looking for user input
            print("Invalid Input. Please answer with 'yes' or 'no'")#prints what is in quotations
            end = input("Would you like to end? yes or no?")#sets end equal to user input
        else:#else statement running code if above if statement is invalid
            break#breaks the while loop
    if end.lower() == "yes":#if statement looking for user input
        for i in nm:#for loop running for each item in nm
            main.append(i)#is appending the item from nm to main
        print("Thank you for viewing the menu. It will now close")#prints what is in quotations
        break#breaks the while loop
