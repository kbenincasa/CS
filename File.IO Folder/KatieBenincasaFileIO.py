'''
Author: Katie Benincasa
Date: 11/29/23
Description: This code reads data and performs 
functions with it according to what the user wants
Imports: -matplotlib for graphing purposes
         -csv for data reading and editing purposes
        -pathlib for file reading
Bugs: This code does not have any bugs I have found
Log: 1/291/2023 - Started mainline
Challenges done: 1, 2, 3, 4, 5, 6, 7, 9, 9a, 9b, 10, 10a, 12, 14
'''
import matplotlib.pyplot as plt 
import csv
from pathlib import Path

new_data = []                       #two empty lists to have data appened to later                                                
students = []

def main():
    '''
    function: This function acts as a menus displaying 
    all the functions available and calls them
    answer: this variables stores the users chosen function
    output: the output is the chosen functions output
    '''
    
    current_dir = Path(__file__).parent
    file_path = current_dir / "gcds_data2.csv"
    file_input = open(file_path)

    
    
    while True:             #loops the options for the program and performs the function until user quits

        print("Menu Enter Choice:")
        print("1) Print All Students in Grade 12")
        print("2) Located Student")
        print("3) View Boys vs Girls")
        print("4) Student Count")
        print("5) Create Graph with Data")
        print("6) Students per Zipcode")
        print("7) Print Students by Last Name")
        print("8) Add Record")
        print("9) Delete Data")
        print("Q) Quit the Program")
        answer = input("Enter a Function:")

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            record_locate(file_input)
        elif answer == "3":
            boys_vs_girls(file_input)
        elif answer == "4":
            student_count(file_input)
        elif answer == "5":
            graph_data(file_input)
        elif answer == "6":
            student_zipcode(file_input)
        elif answer == "7":
            students_sorted(file_input)
        elif answer == "8":
            add_data(file_input)
        elif answer == "9":
            delete_data(file_input)
        elif answer.upper() == "Q":
            print("Bye")
            break
        else:
            print("Invalid Input. Please Try Again.")
        
    file_input.close()

def check_seniors(file_input):
    """ 
    function: finds the amount of seniors in the school
    decision_export: the users decision for exporting to csv 
    output: the names and amount of seniors in the school
    """
    senior_list = []                    #used to add found seniors and write them
    file_input.seek(1)                              

    for record in file_input:
        kid = record.split(",")
        if kid[3] == "12":
            print(kid[0] + " " + kid[2])
            senior_list.append([kid[0], kid[2]])

    decision_export = input("Would you like to export to a csv? Yes or No")
    if decision_export.lower() == "yes":            #exports seniors to csv
        export_csv(senior_list)

    return kid

def record_locate(file_input):
    '''
    function: locates a record in the school's database
    last_name: the users chosen record's last name
    first_name: the users chosen record's first name
    output: the record of a student or 'no match found'
    '''
    last_name = input("Enter last name of student")
    first_name = input("Enter first name of student")

    for record in file_input:
        student_data = record.split(",")
        student_data[2] = student_data[2].lower()
        student_data[0] = student_data[0].lower()
        if student_data[2] == last_name.lower() and student_data[0] == first_name.lower():
            print("First Name:", student_data[0],"Middle Name:", student_data[1], "Last Name:", student_data[2], "Grade:", student_data[3], "Sex:", student_data[4], "Advisor", student_data[5], student_data[6], "State:", student_data[8], "City:", student_data[7], "Zipcode:", student_data[9])
    else:
        print("No Match Found.")

def boys_vs_girls(file_input):
    '''
    function: compares the boys vs girl in the school
    output: the amount of boys and girls
    '''
    female_count = 0
    male_count = 0

    for record in file_input:
        kid = record.split(",")
        if kid[4] == "F":
            female_count += 1
        else:
            male_count += 1
    print("Boys:", male_count)
    print("Girls:", female_count)

def student_count(file_input):
    '''
    function: finds the amount of students in the school
    output: the amoutn of students in the school
    '''
    for record in file_input:
        kid = record.split(",")
        students.append(kid)

    print(len(students))

def graph_data(file_input):
    '''
    function: graphs the amount of students for every grade
    output: the graph of students per grade
    '''
    classes = {"N":0, "PK":0, "K":0, "1":0, "2":0, "3":0, "4":0, 
               "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0}
    first = True

    for record in file_input:
        if first:
            first = False
            continue
        kid = record.split(",")
        classes[str(kid[3])] += 1

    fig = plt.figure(figsize = (10, 5))         #creates the figure for the graph to be on
    x = list(classes.keys())
    y = list(classes.values())
    plt.bar(x, y, width = 0.4, color = 'pink')
    plt.xlabel('x - Grades') 
    plt.ylabel('y - Number of Students') 
    plt.title('The Number of Students in Each Grade') 
    plt.show() 
    
def student_zipcode(file_input):
    '''
    function: finds the amount of students from a certain zipcode
    zipcode: the zipcode chosen by the user
    decision_export: the users responce to exporting data
    output: the amount of students in that zipcode or 'no matches found'
    '''
    zip_data = []       #empty list used to write data to csv
    zip_count = 0
    zipcode = input("Enter Zipcode")
    zipcode = (str(zipcode)).lstrip('0')    #strips zipcode of first 0 i.e. '06830'->'6830'
    zip_data.append(zipcode)
    first = True

    for record in file_input: 
        if first:           #skips first line of csv file
            first = False
            continue
        line = record.split(",")
        if line[9][:-1] == zipcode:
            zip_count +=1
    if zip_count == 0:
            print("No Matches Found")
    zip_data.append(str(zip_count))
    print(zip_count)

    decision_export = input("Would you like to export this data? Yes or no?")
    if decision_export.lower() == "yes":
        export_csv(zip_data)

def students_sorted(file_input):
    '''
    function: sorts the students by last name
    output: prints the students in the school by last name
    '''
    for line in file_input:
        record = line.split(",")
        print(record[0], record[2])
        
def add_data(file_input):
    '''
    function: add a record to the school data
    new_firstname: user input of new first name for record
    new_lastname:nuser input of new last name for record
    new_middlename: user input of new middle name for record
    new_class:user input of new class for record
    new_sex: user input of new sex name for record
    new_advisor_last: user input of new advisor name for record
    new_advisor_first: user input of new advisor name for record
    new_city: user input of new city name for record
    new_state: user input of new state name for record
    new_zipcode: user input of new zipcode name for record
    output: a csv file with the updated records
    '''
    new_firstname = input("Enter new First Name")
    new_lastname = input("Enter new Last Name")
    new_middlename = input("Enter new Middle Name")
    new_class = input("Enter the Class of the Student")
    new_sex = input("Enter the Sex of the New Student")
    new_advisor_last = input("Enter the Last Name of the Advisor")
    new_advisor_first = input("Enter the First Name of the Advisor")
    new_city = input("Enter the City of the Student")
    new_state = input("Enter the State of the Student")
    new_zipcode = input("Enter the Zipcode of the Student")
    new_data.extend([new_firstname, new_lastname, new_middlename, new_class, new_sex, 
    new_advisor_last, new_advisor_first, new_city, new_state, new_zipcode])

    with open('gcds_data2_extra.csv', 'w', newline='') as file:  #using csv.writer to write the list to the CSV file
        writer = csv.writer(file)
        writer.writerow(new_data)

    print("New Record Added.")
    file.close

def delete_data(file_input):
    '''
    function: finds what name is to be deleted, makes a list, iterate through the file 
    check if its the name, if it is continue - if it's not then append the row to the list,
    overite the file and add each item of the list to it
    remoce_name_last: the last name of the record to be deleted
    remove_name_first: the first name of the record to be deleted
    '''
    file_input.seek(1)
    remove_name_last = input("Input Last name of the record to be deleted")
    remove_name_first = input("Input First name of the record to be deleted")
    new_name_list = []          #empty list to add all previous names except deleted

    for record in file_input:
        kid = record.split(",")
        try:        #ads all kids to new list except kid with name to be deleted
            a = kid[2]
        except:
            print(kid)
        if kid[2] == remove_name_last and kid[0] == remove_name_first:
            continue
        else:
            new_name_list.append(record)
            
    with open('gcds_data2_extra.csv', 'w', newline='') as file:     
        writer = csv.writer(file)
        for i in new_name_list:
            a = i.split(",")
            a[-1] = a[-1][:-1]
            writer.writerow(a)

def export_csv(input_):
    '''
    function: writes the output of a functino to a csv
    output: csv file with outputted data written to it
    '''
    with open('Data_Exported.csv', 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ' ')
        for r in input_:
            my_writer.writerow(r)


if __name__ == '__main__':
    main()