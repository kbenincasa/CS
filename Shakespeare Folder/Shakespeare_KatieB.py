'''
Author: Katie Benincasa
Date: 3/4/24
Description: This code compares the ten most frequent words of romeo and juliet to macbeth, that are valuable, in graph form
Imports: string for word gathering, matplotlib for graphing, and counter for sorting dictionaries.
Bugs: There were certain letters that were recognized as words in the .txt but were not there when searched
    -solved by adding a delete command to remove them and now not an issue
Log: 3/4/24 - Started mainline
'''
import string
import matplotlib.pyplot as plt 
from collections import Counter
from pathlib import Path
sorted_r_j = {} # empty dictoinary to store valuable words later
sorted_macbeth = {} # empty dictionary to store valuable words later

def main():
    '''
    function: menu displaying options for user to choose from
    macbeth = the .txt script for macbeth
    romeo_and_juliet = the .txt script for romeo and juliet
    graph_choice = users choice from the menu
    output: the users choice of either graph or to quit
    '''

    current_dir = Path(__file__).parent
    macbeth = current_dir / "macbeth_script.txt"
    romeo_and_juliet = current_dir / "romeo_juliet_script.txt"
    print(romeo_and_juliet)
    macbeth = open(macbeth, "r")
    romeo_and_juliet = open(romeo_and_juliet, "r")
    romeo_juliet_words(romeo_and_juliet, sorted_r_j)
    macbeth_words(macbeth)

    while True:
        graph_choice = input("What graph would you like to see? 1 for Macbeth and 2 for Romeo and Juliet. Q to Quit")
        if graph_choice == "1" or graph_choice == "2":
            if graph_choice == "1":
                macbeth_graph(sorted_macbeth)
            if graph_choice == "2":
                romeo_juliet_graph(sorted_r_j)
        elif graph_choice.upper() == "Q":
            break
        else:
            print("Input Error. Please enter a 1 or 2.")

def romeo_juliet_words(romeo_and_juliet, sorted_r_j):
    '''
    function: find every words and amount of appearances,
    the most frequent words in romeo and juliet (that are valuable),
    and adds them to a new dictionary to be plotted
    rj_dic = the empty dictionary storing all macbeth words and occurances
    '''
    rj_dic = dict()

    for line in romeo_and_juliet: #for loop that will get each individual word regardless of punctuation
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words: # for loop gathering the frequency of the found words
            if word in rj_dic:
                rj_dic[word] = rj_dic[word] + 1
            else:
                rj_dic[word] = 1
        
    del rj_dic[""]
    del rj_dic["o"]
    
    for word in rj_dic.keys(): #adding the most frequent words that are valuable to new dictionary
        if rj_dic[word] >= 81:
            sorted_r_j[word] = rj_dic[word]

    return sorted_r_j

def macbeth_words(macbeth):
    '''
    function: find every words and amount of appearances,
    the most frequent words in macbeth (that are valuable), and
    adds them to a new dictionary to be plotted
    mac_dic = the empty dictionary storing all macbeth words and occurances
    '''
    mac_dic = dict() 

    for line in macbeth: #for loop that will get each individual word regardless of punctuation
        line = line.strip() 
        line = line.lower() 
        line = line.translate(line.maketrans("", "", string.punctuation)) 
        words = line.split(" ") 
        for word in words: #for loop gathering the frequency of the found words
            if word in mac_dic: 
                mac_dic[word] = mac_dic[word] + 1
            else: 
                mac_dic[word] = 1 

    del mac_dic[""]
    del mac_dic["r"]
    
    mac_dic = Counter(mac_dic)

    for word in mac_dic.keys(): #adding the most frequent words that are valuable to new dictinoary
        if mac_dic[word] >= 34:
            sorted_macbeth[word] = mac_dic[word]

    return sorted_macbeth

def romeo_juliet_graph(sorted_r_j):
    '''
    function: graphs the words of romeo and juliet found with the most appearances
    fig = variable storing the size of the plot
    x = variable storing the words of romeo and juliet to be plotted
    y = variable storing the amount of apperances of the specific words to be plotted
    '''
    fig = plt.figure(figsize = (10, 5))         
    x = list(sorted_r_j.keys())
    y = list(sorted_r_j.values())

    plt.bar(x, y, width = 0.4, color = 'pink')
    plt.xlabel('x - Word') 
    plt.ylabel('y - Number of Appearances') 
    plt.title('The most frequent words in Romeo and Juliet') 
    plt.show()


def macbeth_graph(sorted_macbeth):
    '''
    function: graphs the words of macbeth found with the most appearances
    fig = variable storing the size of the plot
    x = variable storing the words of macbeth to be plotted
    y = variable storing the amount of apperances of the specific words to be plotted
    '''
    fig = plt.figure(figsize = (10, 5))         
    x = list(sorted_macbeth.keys())
    y = list(sorted_macbeth.values())

    plt.bar(x, y, width = 0.4, color = 'pink')
    plt.xlabel('x - Word') 
    plt.ylabel('y - Number of Appearances') 
    plt.title('The most frequent words in Macbeth') 
    plt.show()


if __name__ == '__main__':
    main()