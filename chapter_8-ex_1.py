# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of operators. The statement is:
Look at how the two versions for the calculation of the factorial, using while and for, modify the variable a. 
This is not always wanted, because the calculation of a value for a variable shouldn't make the original variable loose its original value. 
Rewrite both programs to avoid that.
"""

a = 4
factorial = 1
count = 1

while count <= a:
    factorial*=count
    count+=1
print(factorial)

a = 4
factorial = a

for i in range(1, a):
    factorial*= i
print(factorial)