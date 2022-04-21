import random
import string
import os
import sys

# If you wanna change the min or max length of the password, cheange min_leng, max_length, and the array of the beggining
# passwordFinal = [' ', ' ', ' ',' ', ' ', ' ', ' '] 
# It's a really simple program :]

print("""  _______  _            _____  _              _        
 |__   __|| |          |  __ \(_)            | |       
    | |   | |__    ___ | |__) |_   ___  ___  | |  ___  
    | |   | '_ \  / _ \|  ___/| | / __|/ _ \ | | / _ \ 
    | |   | | | ||  __/| |    | || (__| (_) || || (_) |
    |_|   |_| |_| \___||_|    |_| \___|\___/ |_| \___/\[T]/ """)
print("\n************************************************************")
print("Welcome to a REALLY simple password maker program")

simbols = ["!", '"' , "#", "$", "%", "&", "(", ")", "+", "/", "<", "=", ">", "?", "@", "{", "|", "}", "~"]
uc = string.ascii_uppercase # Define random upper
lc = string.ascii_lowercase # Define random lower



min_length = 7 # min passwd lenght
max_lenght = 60 # max passwd lenght

# Options
option_N = 0
option_L = 0
option_U = 0
option_S = 0

type_option = 1
next_part = 0

option_start = 0
option_exit = 0

# Funtion option Menu
def MainMenu():
    print(f"""
Type the options you wanna add to your password (1,2,3,4):
    0 = Option NOT choosed / 1 = Option choosed
    1-    [{option_N}]Numbers
    2-    [{option_L}]lower case
    3-    [{option_U}]UPPER CASE
    4-    [{option_S}]Simbols

    5-    [Continue]
    6-    [Exit]""")

# Calling 1º Menu, just wanted to do a funtion
MainMenu()

stop_while = 1 # stop first while
exit = 0

while not(stop_while == 2):
    type_option = int(input("Option: ")) # Fuck u int ( forgot that it need to be int, and the error was trolling me)
    if type_option == 1:
        option_N += 1
    elif type_option == 2:
        option_L += 1
    elif type_option == 3:
        option_U += 1
    elif type_option == 4:
        option_S += 1
    elif type_option == 5:
        stop_while += 1
    elif type_option == 6:
        sys.exit()

    # I couldn't do this with funtions so fuck it, funtion is on top
    if option_N >= 2:
        option_N = 0
    if option_L >= 2:
        option_L = 0
    if option_U >= 2:
        option_U = 0
    if option_S >= 2:
        option_S = 0

    #Active_Inactive(option_N, option_L, option_U, option_S)
    os.system('cls')
    MainMenu()

any_options = option_S + option_N + option_L + option_U # if any_options = 0, program ends

stop_while_2 = 1
while stop_while_2 == 1:
    print(f"""
    Length of the password
    min lenght {min_length}
    max length {max_lenght}
    """)
    length = int(input("Length: "))
    #if (length.isdigit): I'll check str later, i dont know how to make it work
        #print("Just digits") # When u ask for length, if u give a letter it crash :)
    if (min_length <= length <= max_lenght):
        os.system('cls')
        stop_while_2 += 1
    else:
        os.system('cls')

# Increase the array of the password
add_length = min_length
add_length = length - add_length # To know the amouth of appends we need to do to the main array
placer = length -1 # arrays goes from 0 to length - 1

passwordFinal = [' ', ' ', ' ',' ', ' ', ' ', ' '] # min password = 7 # Change it if u want
if add_length != 0:
    for x in range(0, add_length):
        passwordFinal.append(" ") # Increase the length of the passwd

# Generate password
# It make a random number and place the options in the given positions
# And if that spot is taken, it'll make a new random and try again till there is a free one 
if any_options == 0:
    print("No options, no password hihi hiha") # :)
else:
    end = int(0)
    while end < length:
        if option_N == 1:
            done = 1
            if end == length:
                done += 1
            while done != 2:
                charPlacer =  random.randint(0, placer) # Place between 0, and length - 1, for the array
                if passwordFinal[charPlacer] == ' ':
                    rannum = random.randint(0, 9)
                    passwordFinal[charPlacer] =  rannum
                    done += 1
                    end += 1
        
        if option_L == 1:
            done = 1
            if end == length:
                done += 1
            while done != 2:
                charPlacer =  random.randint(0, placer) # Place between 0, and length - 1, for the array
                if passwordFinal[charPlacer] == ' ':
                    ranLC = random.choice(lc)
                    passwordFinal[charPlacer] =  ranLC
                    done += 1
                    end += 1

        if option_U == 1:
            done = 1
            if end == length:
                done += 1
            while done != 2:
                charPlacer =  random.randint(0, placer) # Place between 0, and length - 1, for the array
                if passwordFinal[charPlacer] == ' ':
                    ranUC = random.choice(uc)
                    passwordFinal[charPlacer] =  ranUC
                    done += 1
                    end += 1

        if option_S == 1:
            done = 1
            if end == length:
                done += 1
            while done != 2:
                charPlacer =  random.randint(0, placer) # Place between 0, and length - 1, for the array
                if passwordFinal[charPlacer] == ' ':
                    ransimbols = random.choice(simbols)
                    passwordFinal[charPlacer] =  ransimbols
                    done += 1
                    end += 1

# Read the array, and add it to a empty string                   
TheFinalOne = ""
for a in passwordFinal:
    TheFinalOne += str(a)
print(TheFinalOne)