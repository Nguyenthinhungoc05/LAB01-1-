# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:05:25 2024

@author: DELL
"""

hh = int(input("Nhap vao gio (0 den 23): "))
mm = int(input("Nhap vao phut (0 den 59): "))
ss = int(input("Nhap vao giay (0 den 59): "))
if 0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59:
    print("Thoi gian: ", hh,":",mm,":",ss)
else:
    print("Khong hop le")