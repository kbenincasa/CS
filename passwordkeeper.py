#Creator: Katie Benincasa
#Date: 4.13.23
#Description: This code allows the user to store data regarding login information and access it again
#Bugs: There are no bugs
#Challenges: This code shows the strength of passwords, allows the user to store their login information, and open an excel spreadsheet displaying all information inputted.
#Sources: No additional sources were used outside of what was provided in class



websites = []#makes a list called websites
usernames = []#makes a list called usernames
passwords = []#makes a list called passwords

website_file = open("website_information.csv")#sets the varialbe equal to the file website_information opened
for line in website_file.readlines()[1:]:#creates a for loop for every line in the opened file starting at the second line
    line = line.rstrip()#sets varialbe line equal to the line that is stripped of white from the function
    data = line.split(",")#sets varialbe data equal to lines split with a comma
    websites.append(data[0])#appends the lines of data to websites
    usernames.append(data[1])#appends the lines from line two to usernames
    passwords.append(data[2])#appends the lines of data from the third line to passwords

while True:#creates an endless loop
    pro = input("Do you want to save a new username and password? yes or no?")#sets variable pro equal to user input
    while True:#creates an endless loop
        if pro.lower() != "yes" and pro.lower() != "no":#creates an if statement looking for input
            print("Invalid Input. Please answer with yes or no.")#prints what is in quotations
            pro = input("Do you want to save a new username and password?")#sets variable pro equal to user input
        if pro.lower() == "yes" or pro.lower() == "no":#creates an if statement looking for user input
            break#breaks the while loop
    if pro.lower() == "yes":    #creates an if statement looking for user input
        web = input("What website is this for?")#sets variable equal to user input
        us = input("What is the username?")#sets variable equal to user input
        ps = input("What is the password?")#sets variable equal to user input
        websites.append(web)#appends the variable to list websites
        usernames.append(us)#appends the variable to list websites
        passwords.append(ps)#appends the variable to the list websites
    sl = input("Do you want to see your usernames and passwords? yes or no?")#sets variable equal to user input
    while True:#creates an endless loop
        if sl.lower() != "yes" and sl.lower() != "no":#creates an if statement looking for user input
            print("Invalid Input. Please answer with yes or no.")#prints what is in quotations
            sl = input("Do you want to see a new username and password?")#sets variable equal to user input
        if sl.lower() == "yes" or sl.lower() == "no":#if statement looking for user input
            break#breaks the while loop
    if sl.lower() == "yes":#if statement looking for user input
        for i in range(len(websites)):#for statement that uses variable index and goes for the length of the list websites
            print("Website:", websites[i])#prints the index of websites 
            print("Username:", usernames[i])#prints the index of usernams
            print("Passwords:", passwords[i])#prints the index of passwords
            print()#prints a line for formating
    st = input("Do you want to see how secure your passwords are?")#variable set to user input
    while True:#creates an endless loop
        if st.lower() != "yes" and st.lower() != "no":#if statement looking for user input
            print("Invalid Input. Please answer with yes or no.")#prints what is in quotations
            st = input("Do you want to see how secure your passwords are?")#sets variable equal to user input
        if st.lower() == "yes" or st.lower() == "no":#if statement looking for user input
            break#breaks the while loop
    if st.lower() == "yes":#if statement looking for user input
        for i in range(len(passwords)):#for statement that uses variable index and the length of list passwords
            l = len(passwords[i])#sets variable equal to the length of the index of passwords
            print("Strength of password", passwords[i],"is:", l)#prints what is in quotations and variables
    ex = input("Would you like to export your passwords to an excel spreadsheet?")#sets variable eqaul to user input
    while True:#creates an endless loop
        if ex.lower() != "yes" and ex.lower() != "no":#if statement looking for user input
            print("Invalid Input. Please answer with yes or no.")#prints what is in quotations
            ex = input("Would you like to export your passwords to an excel spreadsheet?")#sets variable equal to user input
        if ex.lower() == "yes" or ex.lower() == "no":#if statement looking for user input
            break#breaks the while loop
    if ex == "yes":#if statement looking for user input
        website_file = open('website_information.csv','w')#sets variable equal to an open and editable excel file
        string_to_write = "Website,Username,Password\n"#sets variable equal to names of the collums 
        for i in range(len(websites)):#creates a for loop for the length of webites 
            string_to_write += websites[i] + "," + usernames[i] + "," + passwords[i] + "\n"#adds usernames and passwords seperated with commas
        website_file.write(string_to_write)#writes in the file
        website_file.close()#closes the file
    end = input("Do you want to quit?")#sets variable equal to user input
    while True:#creates an endless loop
        if end.lower() != "yes" and end.lower() != "no":#if statement looking for user input
            print("Invalid Input. Please answer with yes or no.")#ptrints what is in quotations
            end = input("Do you want to quit?")#sets variable equal to user input
        if end.lower() == "yes" or end.lower() == "no":#if statement checking for user input
            break#brekas the while loop
    if end.lower() == "yes":#if statement checking for user inpiut
        break#breaks the while loop