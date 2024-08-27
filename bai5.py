# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:20:18 2024

@author: Student
"""
import math
thoigian= input("nhap vao thoi gian hh:mm:ss : ")
hh, mm, ss = map(int,thoigian.split (':'))
print("Doi thoi gian ra giay: ", hh*3600 + mm*60 + ss)