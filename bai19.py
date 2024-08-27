# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:45:37 2024

@author: DELL
"""
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
d = int(input("Nhập d: "))
so_nho_nhat = a
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d
print("So be nhat la: ", so_nho_nhat)
