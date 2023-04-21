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

#import random
import src.commands.B01_RNG as RNG

#function kumpul () -> hasil : string
#Kamus Lokal
"""
pasir, batu, air : integer
material : array of integer
hasil : string
"""
#Algoritma
def kumpul(BahanBangunanData):

    #Debug
    #print("Bahan bangunan awal : ", BahanBangunanData)


    #pasir = random.randint(0,5) 
    #batu = random.randint(0,5)
    #air = random.randint(0,5)
    pasir = RNG.RNG(5) 
    batu = RNG.RNG(5)
    air = RNG.RNG(5)
    material = [pasir,batu,air]
    print("Jin menemukan",pasir,"pasir,",batu,"batu, dan",air,"air.")

    # Hitung Total
    PasirLama = int(BahanBangunanData[1][2])
    BatuLama = int(BahanBangunanData[2][2])
    AirLama = int(BahanBangunanData[3][2])

    PasirTotal = pasir + PasirLama
    BatuTotal = batu + BatuLama
    AirTotal = air + AirLama

    # Masukkan data
    BahanBangunanData[1][2] = str(PasirTotal)
    BahanBangunanData[2][2] = str(BatuTotal)
    BahanBangunanData[3][2] = str(AirTotal)

    return BahanBangunanData

# Debug

#Matriks = [["jenis", "deskripsi", "jumlah"],["pasir","asasfsdf","0"],["batu","asasfsdf","0"],["pasir","air","0"]]
#NewMatriks = kumpul(Matriks)