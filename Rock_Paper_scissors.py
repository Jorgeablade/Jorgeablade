# Rock Paper and Scissors
import random
import time
import os

# Posibles Results
options3 = ["Rock", "Paper", "Scissors"]


def Result(PlayerOption, MachineOption):
    if PlayerOption == MachineOption:
        print("\nDraw")
    elif PlayerOption == "Rock" and MachineOption == "Scissors":
        print("\nPlayer wins :)")
    elif PlayerOption == "Paper" and MachineOption == "Rock":
        print("\nPlayer wins :)")
    elif PlayerOption == "Scissors" and MachineOption == "Paper":
        print("\nPlayer wins :)")
    else:
        print("\nMachine Wins :(")
    print(f" \nYour option: {PlayerOption}")
    print(f"Machine option: {MachineOption}")


playyesno = input("¿Wanna play Rock Paper and Scissors? (yes/no): ")
WantsToPlay = 0
while WantsToPlay != 1:
    if playyesno == "yes":
        MachineOption = random.choice(options3)
        PlayerOption = input("Rock, Paper, o Scissors: ")
        i = 0
        if PlayerOption == "Rock" or PlayerOption == "Paper" or PlayerOption == "Scissors":
                i += 1
        while i != 1: 
            PlayerOption = input("Invalid option, Rock, Paper, or Scissors :")
            if PlayerOption == "Rock" or PlayerOption == "Paper" or PlayerOption == "Scissors":
                i += 1
        Result(PlayerOption, MachineOption)
        Playagain = input("Wanna play again??(yes/no): ")
        os.system('cls')
        if Playagain == "no":
            print("Good Game :)")
            time.sleep(3)
            WantsToPlay+= 1
        elif Playagain != "yes":
            print("Invalid Option, closing the game :)")
            time.sleep(3)
            WantsToPlay+= 1
    elif playyesno == "no":
        print("Good bye :]")
        time.sleep(3)
        WantsToPlay+= 1
    else:
        invalid = 0
        while invalid != 1:
            print("Invalid Option")
            invalidAnswer = input("The option given is invalid, try again? (yes/no): ")
            if invalidAnswer == "no":
                print("Good bye :)")
                time.sleep(3)
                invalid += 1
                WantsToPlay+= 1
            elif invalidAnswer == "yes":
                invalid += 1
                playyesno = "yes"
