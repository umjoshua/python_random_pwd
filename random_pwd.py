# Python program to generate random passwords of desired length to csv file
import random
import string
import csv

length=int(input("Enter password length: "))
n=int(input("Enter number of passwords: "))

for i in range(n):
    pwd_chars = string.digits + string.punctuation + string.ascii_letters
    pwd = ''.join(random.choice(pwd_chars) for _ in range(length))
    with open('passwords.csv', 'a', newline='') as file:
        fwriter = csv.writer(file)
        fwriter.writerow([pwd])
