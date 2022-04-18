import sys
import string


def password_check(passwd):  # Checks password strength
    specialSymbols = string.punctuation
    val = True
    errors = []

    if len(passwd) < 14:  # Check length
        errors.append('- Password must be at least 14 characters long')
        val = False

    if not any(char.isupper() for char in passwd):  # Check for uppercase
        errors.append('- Password must contain both lowercase and uppercase characters')
        val = False

    if not any(char.islower() for char in passwd):  # Check for lowercase
        errors.append('- Password must contain both lowercase and uppercase characters')
        val = False

    if not any(char.isdigit() for char in passwd):  # Check for digits
        errors.append('- Password must contain digits')
        val = False

    if not any(char in specialSymbols for char in passwd):  # Check for special characters
        errors.append(f'- Password must contain at least one punctuation character ({specialSymbols})')
        val = False

    return val, errors


# Main method
def main():
    try:  # Check if a password has been passed
        passwd = sys.argv[1]  # Get password from command line
    except IndexError:
        print('Password not provided. Try again.')
        sys.exit(1)
    result, errors = password_check(passwd)  # Call password_check function

    if result:
        print("Strong password")
    else:
        print("Weak password:")
        print('\n'.join(errors))  # Prints all errors


if __name__ == '__main__':
    main()
