import string
import random


def password_generator(name):
    requirements = get_user_input()
    password = generate_password(requirements)
    output_password(password)


def get_user_input():
    # get the requirements of the password
    length = int(input("How long should the password be?\n"))
    numbers = int(input("At least how many numbers should there be?\n"))
    symbols = int(input("At least how many symbols should there be?\n"))

    requirements = [length, numbers, symbols]
    return requirements


def generate_password(requirements):
    # create the list of usable characters for the password
    alphabet = string.ascii_letters
    digits = list(range(0, 10))
    # cast the digits as str so they can be concatenated to the password
    digit_string = [str(int) for int in digits]
    symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*']
    valid_characters = list(alphabet) + digit_string + symbol_list

    # generate the password

    # initialize the running counts used to verify that the password requirements are met
    number_count = 0
    symbol_count = 0

    while number_count < requirements[1] or symbol_count < requirements[2]:
        # initialize the password
        password = ""

        # get a string of characters as long as the length the user specified
        for i in range(requirements[0]):
            # randomly select chars to make the password
            char = random.randint(0, len(valid_characters) - 1)
            password = password + valid_characters[char]

        # if a number of symbol exists in the password, increment the respective count
        for i in password:
            if i in digit_string:
                number_count += 1
            if i in symbol_list:
                symbol_count += 1

        # if the password doesn't meet the requirements, reset the counts to 0 and try again
        if number_count < requirements[1] or symbol_count < requirements[2]:
            number_count = 0
            symbol_count = 0

    return password


# create or append the password to a file
def output_password(password):
    fo = open("passwords.txt", "a")
    fo.write(password + '\n')
    fo.close()

if __name__ == '__main__':
    password_generator('PyCharm')

