# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:13:29 2024

@author: DELL
"""

import math
a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
a1 = a**1/3
b1 = b**1/3
ab = (a*b)**1/3
print("Gia tri cua bieu thuc la: ", (((a+b)/(a1+b1))-ab)/(((a1-b1)**2)))
