# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of lists and tuples. The statement is:
Write, using list comprehension, how to generate a list with the even numbers between 0 and 99 in a single line of code.
"""
even = [x for x in range(1,100) if x % 2 == 0]
print(even)