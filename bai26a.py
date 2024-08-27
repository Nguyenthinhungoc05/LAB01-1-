# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:03:42 2024

@author: DELL
"""

a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
c = float(input("Nhap c = "))
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print(f"Dach sach theo thu tu tang dan: {a:.0f},{b:.0f},{c:.0f}")