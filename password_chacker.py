# password chaker
# Start of the main script

import re  # Import the regular expression module for checking special characters


# password strength check conditions
# min 8 chars, digit, upper case, lower case, special characters.

def check_password_strength(password):  # Define a function that checks the given password against criteria
    if len(password) < 8:  # Check if the length of the password is less than 8 characters
        return "Weak: password must be at least 8 characters long"  # Return a weak message if the length fails

    if not any(char.isdigit() for char in password):  # Check if the password contains at least one digit
        return "Weak: password must contain a digit"  # Return a weak message if no digit is found

    if not any(char.isupper() for char in password):  # Check if the password contains at least one uppercase letter
        return "Weak: password must contain an uppercase letter"  # Return a weak message if no uppercase letter is found

    if not any(char.islower() for char in password):  # Check if the password contains at least one lowercase letter
        return "Weak: password must contain a lowercase letter"  # Return a weak message if no lowercase letter is found

    # Corrected condition for special characters check.
    # If the password meets all other criteria but is missing a special character, it is "Medium".
    if not re.search(r'[!@#$%^&*()\[\]{}<>.?,]', password):  # Use regex to check for the presence of a special character
        return "Medium: password must contain at least one special character"  # If special character is missing, return medium strength

    return "Strong: your password is secured!"  # If all previous checks pass, the password is strong


def password_checker():  # Define the main user interface function
    print("Welcome to the password chaker!")  # Print a welcome message

    while True:  # Start an infinite loop to continuously prompt the user for passwords
        password = input("Please enter a password (or type 'exit' to quit): ")  # Prompt the user for a password input

        if password.lower() == 'exit':  # Check if the user typed 'exit' (case-insensitive)
            print("Thank you for using this tool")  # Print an exit message
            break  # Exit the 'while True' loop

        result = check_password_strength(password)  # Call the strength check function and store the result
        print(result)  # Print the strength result (Weak, Medium, or Strong)


# run the password checker tool.
# This conditional block ensures that the password_checker() function is only called when the script is run directly (not when imported as a module).
if __name__ == '__main__':
    password_checker()  # Call the main function to start the password checker tool



