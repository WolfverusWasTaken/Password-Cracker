import time
import itertools

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
                timetaken = end - start
                return (timetaken)


pw = input("Key in password here :")
stringType = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
timeAmount = passwordtest(pw, stringType)
print("Password Cracked in %s seconds!" % (timeAmount))
