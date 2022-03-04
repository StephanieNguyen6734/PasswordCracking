import hashlib
from passlib.hash import bcrypt
from urllib.request import urlopen
from libs import pingo
import random
from colored import fg
import sys
import emoji
import string

color = fg('#ffd4d4')
chars = string.printable
chars_list = list(chars)
#choosing Brute force or Dictionary
options = input("Which attack? (B/D)")
#Brute force attack
if options == 'B':

    password = input(color + "Enter your password: ")

    guess_password = ""

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print(emoji.emojize(":bear:") + color +"------------" + str(guess_password) + "------------" + emoji.emojize(":bear:"))

        if (guess_password == list(password)):
            print( color + "Your password is : "+ "".join(guess_password))
            break

else:
    hashvalue = input(color + "Enter a string to hash: ")

#Hash for SHA256
    hashobj2 = hashlib.sha256()
    hashobj2.update(hashvalue.encode())
    print('\n SHA256 Hash: ' + hashobj2.hexdigest())

#hash for MD5
    hashobj1 = hashlib.md5()
    hashobj1.update(hashvalue.encode())
    print('\n MD5 Hash: ' + hashobj1.hexdigest())

#Hash for Bcrypt
    hashobj3 = bcrypt.hash(hashvalue)
    print('\n Bcrypt Hash: ' + hashobj3)

    print("\n\n" + (emoji.emojize(":bear:")+"--------------------------------------"+ emoji.emojize(":bear:")))
#Dictionary attack for SHA256
    crackhash = input("\nPress 1 to crack SHA256, 2 for MD5, 3 for Bcrypt: ")

    if crackhash == '1':
        sha256hash = input("\nEnter Sha256 Hash Value: ")
  
        passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        for i in passlist.split('\n'):
            hashguess = hashlib.sha256(bytes(i, 'utf-8')).hexdigest()
            if hashguess == sha256hash:
                print("Password Found!!!\nThe Password is: " + str(i))
                quit()
            else:
                print("\n" + emoji.emojize(":bear:") + "------------does not match-------------" + emoji.emojize(":bear:"))

        print("Password not in passwordlist")

#Dictionary for MD5
    elif crackhash == '2':
        MD5hash = input("Enter MD5 Hash Value: ")
  
        passlist2 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        for i in passlist2.split('\n'):
            hashguess2 = hashlib.md5(bytes(i, 'utf-8')).hexdigest()
            if hashguess2 == MD5hash:
                print("\n\nPassword Found!!!\nThe Password is: " + str(i))
                quit()
            else:
                print("\n" + emoji.emojize(":bear:") + "------------does not match-------------" + emoji.emojize(":bear:"))

        print("Password not in passwordlist")

#Dictionary for Bcrypt
    elif crackhash == '3':

        wordlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

        words = wordlist.splitlines()

        hash = input(color + 'Enter Bcrypt Hash to crack: ')
        length = len(words)

        correct_word = ""
        found = 0
        for (index, word) in enumerate(words):
            pingo(index, length)
            correct = bcrypt.verify(word, hash)
            if (correct):
                correct_word = word
                found += 1
                break

        if (found == 1):
            print(color + "\n\nPassword Found!!!")
            print(color + "The Password is:", correct_word)
        else:
            print(color + "\n\nUnfortunately, password not found.")
    else:
        print("invalid number") 