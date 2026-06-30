# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of operators. The statement is:
On January this year I had a bank account with 3000€. If I earn 1100€ every month and I have some fixed monthly expenses of 435€, 
How much are my monthly extra expenses if by the end of the year my bank account has a total of 6000€?
"""

january=3000
salary=1100
fixed=salary-435
fixed*=12
extras= (january+fixed)-6000
print(extras/12)