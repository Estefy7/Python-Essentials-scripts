# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:53:13 2021

@author: Estefania
"""

try: 
    x = int(input("Enter a number: "))
    y= 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
    print("THE END.")
    