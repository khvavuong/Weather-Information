import random

print('\nWelcome To Your Password Generator')

chars = 'zxcvbnmasdfghjklqwertyuiiop!@#$%^&*ZXCVBNMASDFGHJKLQWERTYUIOP0123456789,./;'

number = input('\nAmount of passwords to generate: ')
number = int(number)

length = input('\nInput your length passwords: ')
length = int(length)

print('\nHere your passwords: \n')
for pwd in range(number):
    passwords = ''
    for ch in range(length):
        passwords += random.choice(chars)
    print(passwords)