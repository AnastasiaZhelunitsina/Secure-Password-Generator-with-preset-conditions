from random import *

def generate_password(the_length_of_a_password, chars):
    password = []
    if the_length_of_a_password < 20:
        for _ in range(the_length_of_a_password - 5):
            password.append(choice(chars))
        password.append(choice(lowercase_letters))
        password.append(choice(uppercase_letters))
        password.append(choice(punctuation))
        password.append(choice(punctuation))
        password.append(choice(digits))
    else:
        for _ in range(the_length_of_a_password - 6):
            password.append(choice(chars))
        password.append(choice(lowercase_letters))
        password.append(choice(uppercase_letters))
        password.append(choice(punctuation))
        password.append(choice(punctuation))
        password.append(choice(punctuation))
        password.append(choice(digits))
    shuffle(password)
    shuffle(password)
    password = ''.join(password)
    return password

lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
digits = '23456789'
chars = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ'
again = input('If you need to generate a password or multiple passwords, enter "yes", if you want to exit, enter " no":  ')

while again == 'y' or again == 'yes' or again == 'yep' or again == 'ype' or again == 'yse':
    print()
    number_of_passwords = int(input('How many passwords do I need to generate? Enter a number: '))
    the_length_of_a_password = int(input('How long should the password be? Enter the required number of characters: '))
    print()

    passwords = []

    for _ in range(number_of_passwords):
        passwords.append(generate_password(the_length_of_a_password, chars))

    print(*passwords, sep='\n')
    print()
    again = input('If you need to generate a password or multiple passwords, enter "yes", if you want to exit, enter " no": ')
else:
    print('Come back if you need to generate a strong password!')
    exit()





