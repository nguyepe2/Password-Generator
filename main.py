import string
import random


def password_generator(name):
    requirements = get_user_input()
    password = generate_password(requirements)
    output_password(password)


def get_user_input():
    # get the requirements of the password
    length = int(input("How long should the password be?\n"))
    numbers = int(input("How many numbers should there be?\n"))
    symbols = int(input("How many symbols should there be?\n"))
    caps = int(input("How many capital letters should there be?\n"))
    lowers = length - numbers - symbols - caps

    requirements = [length, numbers, symbols, caps, lowers]
    return requirements


def generate_password(requirements):
    # create the list of usable characters for the password
    alphabet = string.ascii_letters
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = list(range(0, 10))
    # cast the digits as str so they can be concatenated to the password
    digit_string = [str(int) for int in digits]
    symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*']

    # generate the characters that will be used in the password
    valid_characters = get_lowercase(requirements[4], lower_case) + get_uppercase(requirements[3], upper_case) + \
        get_digits(requirements[1], digit_string) + get_symbols(requirements[2], symbol_list)

    # initialize the password
    password = ""

    # generate the password by rearranging the order of the valid_characters
    for i in range(requirements[0]):
        pos = random.randint(0, len(valid_characters) - 1)
        password = password + valid_characters[pos]
        valid_characters.pop(pos)
    print(password)

    return password


# get the uppercase letters for the password
def get_uppercase(caps, upper_case):
    # initialize a list to store the uppercase letters
    selected_upper_case = []

    # randomly select uppercase letters to use in the password
    for i in range(caps):
        char = random.randint(0, len(upper_case) - 1)
        selected_upper_case.append(upper_case[char])

    return selected_upper_case


# get the digits for the password
def get_digits(numbers, digit_string):
    # initialize a list to store the uppercase letters
    selected_digits = []

    # randomly select uppercase letters to use in the password
    for i in range(numbers):
        char = random.randint(0, len(digit_string) - 1)
        selected_digits.append(digit_string[char])

    return selected_digits


# get the symbols for the password
def get_symbols(symbols, symbol_list):
    # initialize a list to store the uppercase letters
    selected_symbols = []

    # randomly select uppercase letters to use in the password
    for i in range(symbols):
        char = random.randint(0, len(symbol_list) - 1)
        selected_symbols.append(symbol_list[char])

    return selected_symbols


# get the lowercase letters for the password
def get_lowercase(lowers, lower_case):
    # initialize a list to store the uppercase letters
    selected_lower_case = []

    # randomly select uppercase letters to use in the password
    for i in range(lowers):
        char = random.randint(0, len(lower_case) - 1)
        selected_lower_case.append(lower_case[char])

    return selected_lower_case


# create or append the password to a file
def output_password(password):
    fo = open("passwords.txt", "a")
    fo.write(password + '\n')
    fo.close()


if __name__ == '__main__':
    password_generator('PyCharm')
