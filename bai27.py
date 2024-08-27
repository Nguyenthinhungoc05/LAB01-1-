# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:56:33 2024

@author: DELL
"""

import math
h = input("Nhap hinh muon tinh (n: hinh chu nhat, v: hinh vuong, t: hinh tron): ").lower()
if h == 'n':
    n1 = int(input("Nhap chieu dai: "))
    n2 = int(input("Nhap chieu rong:"))
    print("P = ", (n1+n2)*2 )
    print("S = ", n1*n2)
if h == 'v':
    v1 = int(input("Nhap chieu dai canh hinh vuong: "))
    print("P = ", v1*4 )
    print("S = ", v1**2)
if h == 't':
    r = int(input("Nhap ban kinh hinh tron: "))
    print("P = ", 2*3.14*r)
    print("S = ", 3.14*(r**2))
    
