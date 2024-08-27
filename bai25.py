# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:46:07 2024

@author: DELL
"""

a = input("Nhap 1 chu cai bat ki: ")
if a == a.lower() and len(a) == 1:
    print(a.upper())
elif a == a.upper() and len(a) == 1:
    print(a.lower())
else:
    print("Khong hop le!")
    
