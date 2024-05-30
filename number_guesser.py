#-------------------------------------------------------------------------------
# Name:        number_gusser                                                         
# Purpose:
#
# Author:      RAHUL
#
# Created:     27/05/2024
# Copyright:   (c) RAHUL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import random


play_or_quit = input("Do you want to play? : ").lower()


if play_or_quit != "yes":
    quit()


name = input("Enter your name : ")


print("You have five guesses to guess the correct number!")


number = random.randrange(1, 51)
guss = input("Guss the number between 1 and 50 : ")

hint1 = "Hint : The number is lower."
hint2 = "Hint : The number is higher."


def if_not(no_of_gusses):
    """ Set up condition if the guss is wrong. """
    print("Your guss is incorrect!")
    print("you have", no_of_gusses, "total guss left.")



for _ in range(5):
    guss = int(input("Guess the number between 1 and 50 : "))
    if number == guss:
        print("Your guess is correct!")
        quit()
    elif number < guss:
        print(hint1)
    else:
        print(hint2)
print("Game Over")
print("Your guess is incorrect.")
print("The number is", number, ".")


# if number != int(guss):
#     if_not("four")
# elif number == int(guss):
#     print("Your guss is correct!")
#     quit()
# if number != int(guss):
#     if number < int(guss):
#         print(hint1)
#     elif number > int(guss):
#         print(hint2)
#     guss = int(input("Guss the number between 1 to 50 : "))
#     if number == int(guss):
#         print("Your guss is correct!")
#         quit()
#     elif number != int(guss):
#         if_not("three")
# if number != int(guss):
#     if number < int(guss):
#         print(hint1)
#     elif number > int(guss):
#         print(hint2)
#     guss = int(input("Enter you third guss : "))
#     if number == int(guss):
#         print("Your guss is correct!")
#         quit()
#     elif number != int(guss):
#         if_not("two")
# if number != int(guss):
#     if number < int(guss):
#         print(hint1)
#     elif number > int(guss):
#         print(hint2)
#     guss = int(input("Enter you fourth guss : "))
#     if number == int(guss):
#         print("Your guss is correct!")
#         quit()
#     elif number != int(guss):
#         if_not("one")
# if number != int(guss):
#     if number < int(guss):
#         print(hint1)
#     elif number > int(guss):
#         print(hint2)
#     guss = int(input("Enter you fifth guss : "))
#     if number == int(guss):
#         print("Your guss is correct!")
#         quit()
#     else:
#         print("Game Over")
#         print("Your guss is incorrect.")
#         print("The number is", number,".")
        
        




    
