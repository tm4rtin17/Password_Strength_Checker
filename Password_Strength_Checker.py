import pyinputplus as pyip
import sys
import time

#User inputs a password
def input_password():
    password = pyip.inputPassword("Enter the password you would like to verify. [Enter 'q' at to exit program.]")
    special_char = "!@#$%^&*()-+?_=,<>/"
    pass_length = len(password)
    contains_upper = any(char.isupper() for char in password)
    contains_special = any(char in special_char for char in password)
    if password == 'q': #Ends program
        print("See you next time!")
        time.sleep(1)
        sys.exit()
    else:
        return pass_length, contains_upper, contains_special

#flow control for password requirements
def pass_strength(pass_length, contains_upper, contains_special):
    if pass_length < 6:
        rating = "weak"
    elif pass_length > 6 and pass_length < 8:
        rating = "average"
    elif pass_length >= 8 and pass_length < 12 and contains_upper == True and contains_special == True:
        rating = "strong"
    elif pass_length >= 12 and contains_upper == True and contains_special == True:
        rating = "very strong"
    else:
        rating = "average"
    return rating

#Returns results to the user
def pass_results(rating, pass_length, contains_upper, contains_special):

    #print results of password strength
    print(f"Your password is {rating}")
    
    #if statements to give user reccomendations for how to improve their password
    if pass_length < 12:
        length_delta = 12 - pass_length
        print(f"- Increase password length by {length_delta} characters.")
    if contains_upper == False:
        print("- Add an uppercase letter.")
    if contains_special == False:
        print("- Add a special character or symbol '!@#$%^&*()-+?_=,<>/.'")
    
#Initial Function Call
pass_length, contains_upper, contains_special = input_password()
rating = pass_strength(pass_length, contains_upper, contains_special)
pass_results(rating, pass_length, contains_upper, contains_special)

#While loop for re-runs
while True:
    run_again = pyip.inputYesNo("Would you like to check another password? (y/n)")
    if run_again == "yes":
        #Runs the same 3 functions as the initial calling
        pass_length, contains_upper, contains_special = input_password()
        rating = pass_strength(pass_length, contains_upper, contains_special)
        pass_results(rating, pass_length, contains_upper, contains_special)
    else:
        print("Thanks for keeping your passwords secure!")
        break
