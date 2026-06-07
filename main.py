
import random
import string

print("Welcome to the Password Generator!")
print("Generate secure random passwords instantly.\n")

special_chars = "!@#$%&*"
characters = string.ascii_letters + string.digits + special_chars

password = [random.choice(string.ascii_uppercase),
random.choice(string.ascii_lowercase),
random.choice(string.digits),
random.choice(special_chars)]

length = int(input("Enter the length of password you need to generate:"))

if length < 4:
    print("Password length must be atleast 4")
else :
  

  for i in range(length-4):
    password.append(random.choice(characters))

  random.shuffle(password)
  password = "".join(password)


  print(f"Generated password :  {password}")