# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:55:53 2024

@author: DELL
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print("So lon nhat la: ", so_lon_nhat)