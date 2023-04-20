import random
import string

def get_chars()-> string:
    """get the all alphabets that the user select

    :return: all alphabet selected
    :rtype: string
    """
    all_char = ""
    count = 1
    num = int(input("How many alphabet did u need? (lower, upper, number and special cases)"))
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
        count+=1
    return all_char

def main()-> string:
    """main function

    :return: generated password
    :rtype: string
    """
    result = ""
    i = 0
    chars = get_chars()
    pass_length = int(input("Insert the length of your password: "))
    while i <= pass_length:
        result += random.choice(chars)
        i+=1
    return result


if __name__ == "__main__":
    password = main()
    print(f"Your password is: {password}")

#TODO: graphic interface
#TODO: auto copy password
