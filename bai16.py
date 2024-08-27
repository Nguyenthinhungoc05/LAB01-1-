# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:24:10 2024

@author: DELL
"""

thoigian= input("nhap vao thoi gian hh:mm:ss : ")
hh, mm, ss = map(int,thoigian.split (':'))
print("Doi thoi gian ra giay: ", hh*3600 + mm*60 + ss)