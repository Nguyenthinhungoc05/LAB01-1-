# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:26:44 2024

@author: DELL
"""

import math
a= float(input("Nhap he so a: "))
b= float(input("Nhap he so b: "))
c= float(input("Nhap he so c: "))
delta= b*b - 4*a*c
if a!=0 and delta <0:
    print("Biện luận:")
    print(f"Vì delta = {delta} < 0,phương trình vô nghiệm")
elif a!=0 and delta ==0:
    print("Biện luận:")
    print(f"Vì delta = 0,Phuong trinh co nghiem kep x1=x2= ",-b/2*a)
elif a!=0 and delta >0:
    print("Biện luận:")
    print(f"Vì delta = {delta} > 0, phương trình có hai nghiệm phân biệt:")
    print("x1= ", (-b + math.sqrt(delta))/2*a)
    print("x2= ", (-b - math.sqrt(delta))/2*a )
else:
    print("Khong xac dinh")