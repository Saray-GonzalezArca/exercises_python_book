# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of operators. The statement is:
Modify the code for the calculation of a prime number using loop nesting to automatically obtain prime numbers less than 1 000. 
Take advantage of the option to use else to display only the prime numbers
"""

count = 1
num = 1000
prime = []

for i in range(2, num):
    for e in range(2, i):
        if i % e == 0:
            break
    else:
        prime.append(i)

for i in range(len(prime)):
    print(prime[i])