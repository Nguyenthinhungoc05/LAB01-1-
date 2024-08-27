# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:43:04 2024

@author: Student
"""

import math
so = int(input("Nhap so xe cua ban (co 4 chu so ): "))
ngan = so // 1000
tram = so // 100 % 10
chuc = so // 10 % 10
don_vi = so % 10
so_nut = ngan + tram + chuc + don_vi
a = so_nut // 10
b = so_nut % 10
c = a + b
x = c // 10
y = c % 10
z = x + y
print(f"Bien so cua ban co {z}")
