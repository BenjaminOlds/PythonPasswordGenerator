import random

chars = 'abcdefghijklmnopqrstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()+=_-'
min_length = 8
max_length = 16
password = ""
password_length = (random.randrange(min_length, max_length + 1))

while len(password) < password_length:

    password = password + random.choice(chars)

print('Your password is:', password)
