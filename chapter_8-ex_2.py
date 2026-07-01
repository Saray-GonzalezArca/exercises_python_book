# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of operators. The statement is:
Write a program that iterates over the list of names ["Pedro", "Pablo", "Judas", "Juan"].
Inside the loop, it will check if the name is "Judas".
If so, the program should print the name on the screen along with the text "is guilty"; 
otherwise, it should print the name along with the text "is innocent". The expected output is:
    Pedro is innocent
    Pablo is innocent
    Judas is guilty
    Juan is innocent
"""

names = ["Pedro", "Pablo", "Judas", "Juan"]

for i in range(len(names)):
    if names[i]=="Judas":
        print("Judas is guilty")
    else:
        print(names[i], "is innocent")