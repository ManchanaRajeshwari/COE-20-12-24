import string
def check_password_strength(password):
    if len(password)<10 or len(password)>15:
        return "The password should contain min 10 charecters and max 15 charecters"
    elif not any( char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit for char in password) or not any(char in string.punctuation for char in password):
         return "Should contain above conditions"
    elif any(char.isspace() for char in password ):
        return "The password should not contain any spaces"
    elif (password[-1]== '.' or password[-1]=='@'):
        return "The password should not ends with . or @"
    else:
        return "You entered a valid password"
password=input("Enter password")
print(check_password_strength(password))