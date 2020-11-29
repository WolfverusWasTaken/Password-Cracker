# Imports
import itertools
import time


# Brute force function
def passwordtest(SetPass, SetString):
    start = time.time()
    chars = SetString
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            print(letter,"attempt: ", attempts)
            letter = ''.join(letter)
            if letter == SetPass:
                end = time.time()
                distance = end - start
                return (attempts, distance)


pw = input("Key in password here :")
# Allowed characters
stringType = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
tries, timeAmount = passwordtest(pw, stringType)
print("Password Cracked in %s seconds!" % (timeAmount))