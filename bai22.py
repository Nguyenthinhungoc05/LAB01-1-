# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:13:05 2024

@author: DELL
"""

a = float(input("nhap a: "))
b = float(input("nhap b: "))
if a==0 and b==0:
    print("Biện luận:")
    print("Vì a = 0 và b = 0, phương trình trở thành 0 = 0.")
    print("Đây là một đẳng thức đúng với mọi giá trị của x.")
    print("Suy ra,phuong trinh co vo so nghiem")
elif a==0 and b!=0:
    print("Biện luận:")
    print(f"Vì a = 0 và b = {b} ≠ 0, phương trình trở thành {b} = 0.")
    print("Đây là một đẳng thức vô lý.")
    print("Suy ra, phuong trinh vo nghiem")
else:
    print("Biện luận:")
    print(f"Vì a = {a} ≠ 0, suy ra phuong trinh co nghiem duy nhat: x =  ",-b/a)