# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:00:47 2024

@author: DELL
"""
so = ("Khong", "Mot", "Hai", "Ba", "Bon","Nam","Sau","Bay","Tam","Chin")
a = int(input("Nhap 1 so nguyen bat ky tu 0 den 9: "))
if 0 <= a <= 9:
    print(so[a])
else:
    print("Khong doc duoc")
