import random # getting random module which is inbuilt in python

user_int_I = int(input("Enter the length size of your password: ")) # user input of integer asking the user entering the length of user's password
user_int_II = int(input("Enter the no. of passwords you want to generate: ")) # user input of integer asking user of how many passwords user wants

list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] # *Longest Line* a list of the english alphabet
list_integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # list of numbers
list_symbol = ["!", "@", "#", "$", "%", "^", "&", "*"] # list of symbols
character_list = list_symbol + list_alphabet + list_integers # character list which is combination of list_symbol + list_alphabet + list_integers

for i in range(user_int_II): # for loop in range depending on 2nd user input
    password_character = random.choices(character_list, k=user_int_I)  # choices made by random module(in-built) containing character_list & user input
    password = "".join(password_character)  # joins the password
    print(password) # showing password
