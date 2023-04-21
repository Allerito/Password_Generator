import random
import string
import pyperclip

def get_chars()-> string:
    """get the all alphabets that the user select

    :return: all alphabet selected
    :rtype: string
    """

    all_char = ""

    try:
        num = int(input("How many alphabets do you want? (lower, upper, number and special cases)"))
    except ValueError:
        raise ValueError("Error you need to insert a number")
    if num > 4:
        raise ValueError("Error you can't select more than 4 alphabets")
    elif num == 0 or num < 0:
        raise ValueError("Error you need to select at least 1 alphabet")

    elif num == 4:
        print("You selected all alphabets")
        all_char += string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        return all_char

    while num > 0:
        select_alphabet=input("Which alphabet do you want? (lower, upper, number or special)")
        select_alphabet = select_alphabet.lower()
        
        #! Warning: This doesn't check if the user select the same alphabet twice (will not fix since you won't be able to do it in the graphical interface)
        if select_alphabet == "lower" or select_alphabet == "l":
            all_char += string.ascii_lowercase
        elif select_alphabet == "upper" or select_alphabet == "u":
            all_char += string.ascii_uppercase
        elif select_alphabet == "number" or select_alphabet == "n":
            all_char += string.digits
        elif select_alphabet == "special" or select_alphabet == "s":
            all_char += string.punctuation
        else:
            print("Error you didn't select a valid alphabet, please try again")
            continue

        num -= 1
    return all_char

def generatePassword(characters: string) -> string:
    """main function

    :return: generated password
    :rtype: string
    """

    result = ""
    pass_length = int(input("Insert the length of your password: "))
    if pass_length >= 8 or pass_length <= 64:
        for i in range(pass_length):
            result += random.choice(characters)
        return result
    else:
        raise ValueError("Error your password length needs to be between 8 and 64")

if __name__ == "__main__": 
    try:
        characters = get_chars()
        password = generatePassword(characters)
        pyperclip.copy(password)
        print(f"Your password is: {password}")
    except ValueError as e:
        print(e)
        
#TODO: graphic interface
