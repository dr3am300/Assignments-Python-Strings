# Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. 
# If not, print an error message.


def input_length_validator():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error !!!! Both first and last names should be at least 2 characters long.")
    else:
        print("Thank you for providing your name.")
input_length_validator()


