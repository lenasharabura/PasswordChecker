import string
import random

DIGITS = string.digits
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
SYMBOLS = string.punctuation
COMBINATIONS = DIGITS + LOWER_CASE + UPPER_CASE + SYMBOLS


def generate_password():  # Generates a random password

    length = 14  # length of password to generate

    rand_digit = random.choice(DIGITS)  # random digit
    rand_upper = random.choice(UPPER_CASE)  # random upper case letter
    rand_lower = random.choice(LOWER_CASE)  # random lower case letter
    rand_symbol = random.choice(SYMBOLS)  # random symbol
    password = list(rand_digit + rand_upper + rand_lower + rand_symbol)  # mandatory part of the password

    for i in range(length - 4):  # random characters
        password.append(random.choice(COMBINATIONS))

    random.shuffle(password)  # shuffling the resultant password
    return ''.join(password)  # converting the list to string


# Main function
def main():
    password = generate_password()
    print(password)


if __name__ == '__main__':
    main()
