import random

print("Welcome to your password generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,'
nums = '0123456789'
allChars = chars + nums

#prompt to enter how many passwords you need to generate
number = input("Amount of passwords to generate: ")
number = int(number)

#prompt to enter the length for your passwords
length  = input("Input your password length: ")
length = int(length)

#prints your passwords
print('\nhere are your passwords:')

#the for loop for generating individual passwords and printing them
for password in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(allChars)
    print(passwords)
