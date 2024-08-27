# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:29:27 2024

@author: DELL
"""

import math
a = input("Nhap vao gio thu nhat(h1:m1:s1): ")
b = input("Nhap vao gio thu hai(h2:m2:s2): ")
h1,m1,s1 = map(int,a.split(':'))
h2,m2,s2 = map(int,b.split(':'))
print("Tong hai gio = ",(h1 + h2),":",(m1 + m2),":",(s1 + s2))
print("Hieu hai gio = ",(h1 - h2),":",(m1 - m2),":",(s1 - s2))