# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise input and output. The statement is:
Write a program that asks the user their and their friend's age. The program will show who is older.
"""
uage = int(input("How old are you? "))
fage = int(input("How old is your friend? "))

if uage > fage:
    print("You are older than your friend.")
elif uage < fage:
    print("Your friend is older than you.")
else:
    print("You have the same age")