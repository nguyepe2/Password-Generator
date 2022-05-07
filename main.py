import string
import random
import tkinter


# start of tkinter


top = tkinter.Tk()


# create text label for password length input field
length_label = tkinter.Label(top, text = "Password Length")
length_label.pack()

# create input field for length
length_entry = tkinter.Entry(top)
length_entry.pack()
length_entry.insert(0, 20)

# create text label for number length input field
number_label = tkinter.Label(top, text = "Amount of numbers")
number_label.pack()

# create input field for number length
number_entry = tkinter.Entry(top)
number_entry.pack()
number_entry.insert(0, 2)


# create text label for symbol length input field
symbol_label = tkinter.Label(top, text = "Amount of symbols")
symbol_label.pack()

# create input field for symbol length
symbol_entry = tkinter.Entry(top)
symbol_entry.pack()
symbol_entry.insert(0, 2)


# create text label for caps length input field
caps_label = tkinter.Label(top, text = "Amount of capitals")
caps_label.pack()

# create input field for caps length
caps_entry = tkinter.Entry(top)
caps_entry.pack()
caps_entry.insert(0, 2)

def password_generator():
    requirements = get_user_input()
    password = generate_password(requirements)
    output_password(password)



def get_user_input():
    # get the requirements of the password
    length = int(length_entry.get())

    numbers = int(number_entry.get())

    symbols = int(symbol_entry.get())

    caps = int(caps_entry.get())

    lowers = length - numbers - symbols - caps

    requirements = [length, numbers, symbols, caps, lowers]

    return requirements


start = tkinter.Button(top, text="Run", command=password_generator)
start.pack()


copied_label = tkinter.Label(top, text="")
copied_label.pack()


# create empty placeholder text label for generated password
password_label = tkinter.Label(top, text=" ")
password_label.pack()


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

    # fill password label placeholder with actual password
    password_label.config(text=password)

    copied_label.config(text="Password copied to clipboard!")


    # clear the clipboard
    top.clipboard_clear()
    # copy generated password to clipboard
    top.clipboard_append(password)

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
    # initialize a list to store the digits
    selected_digits = []

    # randomly select digits to use in the password
    for i in range(numbers):
        char = random.randint(0, len(digit_string) - 1)
        selected_digits.append(digit_string[char])

    return selected_digits


# get the symbols for the password
def get_symbols(symbols, symbol_list):
    # initialize a list to store the symbols
    selected_symbols = []

    # randomly select symbols to use in the password
    for i in range(symbols):
        char = random.randint(0, len(symbol_list) - 1)
        selected_symbols.append(symbol_list[char])

    return selected_symbols


# get the lowercase letters for the password
def get_lowercase(lowers, lower_case):
    # initialize a list to store the lowercase letters
    selected_lower_case = []

    # randomly select lowercase letters to use in the password
    for i in range(lowers):
        char = random.randint(0, len(lower_case) - 1)
        selected_lower_case.append(lower_case[char])

    return selected_lower_case


# create or append the password to a file
def output_password(password):
    fo = open("passwords.txt", "a")
    fo.write(password + '\n')
    fo.close()


top.mainloop()






