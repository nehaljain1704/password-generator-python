
import random
import string


special_chars = "!@#$%&*"
characters = string.ascii_letters + string.digits + special_chars

length = int(input("Enter the length of password you need to generate:"))

if length <= 0:
    print("Password length must be greater than 0")
else :
  password = ""

  for i in range(length):
    password += random.choice(characters)


  print(f"Generated password :  {password}")