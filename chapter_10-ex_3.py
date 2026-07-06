# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise the use of lists and tuples. The statement is:
The following code belongs to a program that calculates the rainiest month from a monthly record in liters.
You must complete this code by replacing the bold comments with the appropiate list operations for the correct execution of the program.
Line 14: # Calculate the maximum recorded rainfall value here.
Line 15: # get the index of the corresponding month.
"""

mensual_rain = [65, 70, 87, 62, 44, 14, 5, 5, 24, 50, 57, 69]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "dicember"]

max_rain = max(mensual_rain)
month_max = mensual_rain.index(max_rain)

print(f"El mes más lluvioso ha sido {months[month_max]} con {max_rain} litros.")