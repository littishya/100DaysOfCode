# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:40:36 2022  9:40 -9:50pm

@author: 2063176

Medium 
Project 1: CREATE ACRONYMS USING PYTHON
"""
user_input = str(input("Enter a Phrase:"))
text = user_input.split()
a =""
for i in text:
    a = a+str(i[0]).upper()
print(a)
