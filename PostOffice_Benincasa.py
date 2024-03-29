'''
Author: Katie Benincasa
Date: 9/12/23
Description: This program takes the length, width, and height of a package
 as well as the starting and ending zip code and returns the cost to ship it.
Bugs: None
'''

for i in range(0,5):  


    def main():    
        '''
        function: takes the inputs, runs all the other functinos, and uses the data raceived
        to produce and print the final output.
        data:sets variable data equal to the input and splits the data between every comma
        length: sets the first item in data to the variable length
        height: sets the second item in data to the variable height
        width: sets the third item in data to variable width
        start: sets the fourth item in data to variable start
        end: sets the fifth item in data to variable end
        output: the cost of the package
        '''   
        try:                                                            
            data = input("Enter the data:")                                           
            data = data.split(",")                                                          
            length = float(data[0])                                                         
            height = float(data[1])                                                         
            width = float(data[2])                                                          
            start = float(data[3])                                                          
            end = float(data[4])                                                            
            size = get_classification(length, width, height)                                               
            start_zone, end_zone = get_zone(start, end)   
            difference = abs(end_zone - start_zone)                                      
            print((get_cost_package(size, difference)))
        except:                                                       
            print("Error.")
        

    def get_classification(length, width, height):    
        '''
        function: this function uses the length, width, and height
        input and uses it to get the class of the mail
        length: used to calculate package class
        width: used to calculate package class
        height: used to calculate package class
        output: the class of the package class set to variable 'classy'
        '''
        perimiter = 2*(length + width + height)
        perimiter = float(perimiter)
        #
        if  4.25 >= length >= 3.5 and 6 >= height >= 3.5 and .016 >= width >= .007: 
            classy = "Regular Post Card"
        elif 6 > length > 4.25 and 11.5 > height > 5 and .015 >= width >= .007:
            classy = "Large Post Card"
        elif 6.125 >= length >= 3.5 and 11.5 >= height >= 5 and .25 > width > .016:
            classy = "Envelope"
        elif 24 > length > 6.125 and 18 >= height >= 11 and .5 >= width >= .25:
            classy = "Large Envelope"
        elif (length > 24 or height > 18 or width > .5) and perimiter <= 84:
            classy = "Package"
        elif 130 > perimiter > 84:
            classy = "Large Package"
        else:
            classy = "Unmailabe"
        return classy

    
    def get_zone(start, end):  
        '''
        function: this function uses the start and end input to 
        return the zone the mail is going to and the zone it came from
        start: used to calculate the start zone of the package
        end: used to calculate the end zone of the package
        output: the start and end zones of the package
        '''                                                      
        if 6999 >= start > 0:
            start_zone = 1
        elif 19999 >= start >= 7000:
            start_zone = 2
        elif 35999 >= start >= 20000:
            start_zone = 3
        elif 62999 >= start >= 36000:
            start_zone = 4
        elif 84999 >= start >= 63000:
            start_zone = 5
        elif 99999 >= start >= 85000:
            start_zone = 6
        if 6999 >= end >= 1:
            end_zone = 1
        elif 19999 >= end >= 7000:
            end_zone = 2
        elif 35999 >= end >= 20000:
            end_zone = 3
        elif 62999 >= end >= 36000:
            end_zone = 4
        elif 84999 >= end >= 63000:
            end_zone = 5
        elif 99999 >= end >= 85000:
            end_zone = 6
        else:
            "Invalid Ending Zip Code"
        return start_zone, end_zone
    

    def get_cost_package(size, difference):   
        '''
        function: this function uses the zones the packages starting and ending zones 
        to calculate the final cost to mail the package and returns it
        size: used to calculate the base cost of shipping the package
        difference: used to calculate the addition cost from mailing across zones
        output: the output is the total cost to mail the package
        '''                                       
        x = 1
        if size == "Regular Post Card":
            package_cost = .2
        elif size == "Large Post Card":
            package_cost = .37
        elif size == "Envelope":
            package_cost = .37
        elif size == "Large Envelope":
            package_cost = .6
        elif size == "Package":
            package_cost = 2.95
        elif size == "Large Package":
            package_cost = 3.95
        if size == "Regular Post Card":
            cost = package_cost + difference*(.03)
        elif size == "Large Post Card":
            cost = package_cost + difference*(.03)
        elif size == "Envelope":
            cost = package_cost + difference*(.04)
        elif size == "Large Envelope":
            cost = package_cost + difference*(.05)
        elif size == "Package":
            cost = package_cost + difference*(.25)
        elif size == "Large Package":
            cost = package_cost + difference*(.35)
        #this section is converting the price to be accurate in dollars and cents
        cost = str(round(cost, 3))
        cost = '{:,.2f}'.format(float(cost))
        if cost[0] == "0":
            cost = cost[1:]
        return cost
        
        
    if __name__ == '__main__':
        main()