import random
import string

password = ""
all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

pass_length = int(input("Insert the length of your password: "))
for i in range(pass_length):
    password += random.choice(all_char)

print(f"Your password is: {password}")

#TODO: choices about the chars
#TODO: graphic interface
#TODO: auto copy password