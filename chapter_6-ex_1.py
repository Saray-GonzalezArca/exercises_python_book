# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of operators. The statement is:
My car consumes 5.5 liters every 100km and my work is 15km far away from my home. 
How much will I spend in gasoline in 20 work days if the price is 1.12€/L?
"""

distance= (15*2*5.5)/100

total_liters = distance*20
price = total_liters*1.12

print("The total amount of money spent in gasoline during 20 work days will be:", price)