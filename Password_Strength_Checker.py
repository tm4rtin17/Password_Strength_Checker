import pyinputplus as pyip

#Define check password function
def check_password():
    password = pyip.inputPassword("Enter the password you would like to verify.")
    special_characters = "!@#$%^&*()-+?_=,<>/"
    password_length = len(password)
    password_contains_uppercase = any(char.isupper() for char in password)
    password_contains_special = any(char in special_characters for char in password)
    password_strength = ""
    
    #flow control for password requirements
    if password_length < 6:
        password_strength = "weak"
    elif password_length > 6 and password_length < 8:
        password_strength = "average"
    elif password_length >= 8 and password_length < 12 and password_contains_uppercase == True and password_contains_special == True:
        password_strength = "strong"
    elif password_length >= 12 and password_contains_uppercase == True and password_contains_special == True:
        password_strength = "very strong"
    else:
        password_strength = "average"

    #print results of password strength
    print(f"Your password is {password_strength}")
    
    #if statements to give user reccomendations for how to improve their password
    if password_length < 12:
        length_delta = 12 - password_length
        print(f"- Increase password length by {length_delta} characters.")
    if password_contains_uppercase == False:
        print("- Add an uppercase letter.")
    if password_contains_special == False:
        print("- Add a special character or symbol (!@#$%^&*()-+?_=,<>/).")
    

check_password()