# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise input and output. The statement is:
Make a program that asks for an integer to the user and shows the next five numbers, right-justified.
"""

num = int(input("Write an integer: "))

for i in range(1,6):
    print(str(num+i).rjust(50))