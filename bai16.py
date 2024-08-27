# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:24:10 2024

@author: DELL
"""
thoigian= input("nhap vao thoi gian ..h..p..s: ")
so = ""
for i in thoigian:
    if i.isalpha():
        so += ":"
    else:
        so += i
so_cuoi = so[:-1]
hh,mm,ss = map(int,so_cuoi.split (':'))
print(thoigian,"thi doi ra giay bang ", hh*3600 + mm*60 + ss)
