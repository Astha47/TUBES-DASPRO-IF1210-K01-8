#(butuh revisi)
#def kumpul()
#    return hasil

#F02 - Kumpul

#SPESIFIKASI DAN DEFINISI

"""
material : {  pasir : integer
                batu  : integer
                air   : integer }
"""

#function kumpul () -> hasil : string
#{fungsi ini akan menghasilkan kumpulan material (pasir, batu, dan air) dengan nilai yang random antara 0-5
#untuk membangun candi dan menyimpan nilai hasil kumpulan material dalam sebuah array bernama 'material'}

#REALISASI

import random

#function kumpul () -> hasil : string
#Kamus Lokal
"""
pasir, batu, air : integer
material : array of integer
hasil : string
"""
#Algoritma
def kumpul():
    pasir = random.randint(0,5) 
    batu = random.randint(0,5)
    air = random.randint(0,5)
    material = [pasir,batu,air]
    hasil = "Jin menemukan {} pasir, {} batu, dan {} air".format(pasir,batu,air)
    return hasil
print(kumpul()) 