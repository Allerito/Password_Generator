import random
import string
import pyperclip

__ERROR__ = False

def get_chars()-> string:
    """get the all alphabets that the user select

    :return: all alphabet selected
    :rtype: string
    """
    all_char = ""
    count = 1
    num = int(input("How many alphabet do you want? (lower, upper, number and special cases)"))
    if num >= 1 or num <= 4:
        while count <= num:
            select_alphabet=input("Which alphabet do you want? (lower, upper, number or special)")
            if select_alphabet == "lower" or select_alphabet == "Lower" or select_alphabet == "LOWER" or select_alphabet == "l" or select_alphabet == "L":
                all_char += string.ascii_lowercase
            elif select_alphabet == "upper" or select_alphabet == "Upper" or select_alphabet == "UPPER" or select_alphabet == "u" or select_alphabet == "U":
                all_char += string.ascii_uppercase
            elif select_alphabet == "number" or select_alphabet == "Number" or select_alphabet == "NUMBER" or select_alphabet == "n" or select_alphabet == "N":
                all_char += string.digits
            elif select_alphabet == "special" or select_alphabet == "Special" or select_alphabet == "SPECIAL" or select_alphabet == "s" or select_alphabet == "S":
                all_char += string.punctuation
            else:
                print("Error you didn't select a correct alphabet")
            count+=1
        return all_char
    else:
        print("Error you can't select more than 4 alphabets")
        global __ERROR__
        __ERROR__  = True

def main()-> string:
    """main function

    :return: generated password
    :rtype: string
    """
    global __ERROR__
    result = ""
    i = 1
    chars = get_chars()
    if not __ERROR__:
        pass_length = int(input("Insert the length of your password: "))
        if pass_length >= 8 or pass_length <= 64:
            while i <= pass_length:
                result += random.choice(chars)
                i+=1
            return result
        else:
            print("Error your password need to be length a value between 8 and 64")
            __ERROR__ = True

if __name__ == "__main__":
    if not __ERROR__:
        password = main()
        pyperclip.copy(password)
        print(f"Your password is: {password}")
    else:
        print("An error was occured")

#TODO: graphic interface
