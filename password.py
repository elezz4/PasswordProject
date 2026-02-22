import random
from random import shuffle

letters = [
    # lowercase
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

digits = ['0','1','2','3','4','5','6','7','8','9']

characters = ['!','"','#','$','%','&',"'",'(',')','*','+', ',', '-', '.', '/', ':',';','<','=','>','?', '@','[',']','^','_','`','{','|','}','~']

password = []

amount_letters = int(input("How many letter do you want ? "))
amount_digits = int(input("How many digits do you want ? "))
amount_characters = int(input("How many letter do you want ? "))

for letter in range(0, amount_letters):
    password.append(random.choice(letters))

for digit in range(0, amount_digits):
    password.append(random.choice(digits))

for char in range(0, amount_characters):
    password.append(random.choice(characters))

random.shuffle(password)

print("Your password: ")

for char in password:
    print(char, end = "")








