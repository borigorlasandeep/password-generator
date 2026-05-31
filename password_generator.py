import random
import string

pass_len = int(input("Enter password length: "))

char_values = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(char_values) for _ in range(pass_len))

print("Your random password is:", password)