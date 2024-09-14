import random
import string
len_pass = 3
charVal = string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(len_pass):
    password += random.choice(charVal)

print("Your strong password is: ", password)