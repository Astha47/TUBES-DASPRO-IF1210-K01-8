"""
Total Candi: 3
Total_Pasir : 11
Total_Batu : 12
Total_Air : 16
ID Candi Termahal: 3 (Rp 212500)
ID Candi Termurah: 1 (Rp 97500)
"""

#"""
# Def AmbilLaporanCandi
# F10 - Ambil Laporan Candi
# Fungsi menerima info candi lalu memberikan informasi total candi terbangun, bahan-bahan material yang digunakan, dan ID dari candi termahal dan termurah beserta harganya.

# KAMUS

# ALGORITMA
def hitungIsi(CandiData, BarisCandi):  # Fungsi F06
    isi = 0
    for i in range (1,BarisCandi):
        if CandiData[i][0] != '':
            isi += 1
    return isi

# Menghitung Material dari CandiData
def Material(CandiData, BarisCandi):
    Total_Pasir = 0
    Total_Batu = 0
    Total_Air = 0
    for i in range (1,BarisCandi):
        if (CandiData[i][0]) != '':
            Total_Pasir += int(CandiData[i][2])
            Total_Batu  += int(CandiData[i][3])
            Total_Air   += int(CandiData[i][4])
    print("Total_Pasir :" , Total_Pasir)
    print("Total_Batu :" , Total_Batu)
    print("Total_Air :" , Total_Air)

# Menghitung Harga Candi 
def HargaCandi(CandiData, i):
    if CandiData[i][2] != '':
        return(10000*int(CandiData[i][2]) + 15000*int(CandiData[i][3]) + 7500*int(CandiData[i][4]))
    else:
        return(0)

# Menentukan Candi Termahal
def CandiTermahal(CandiData, BarisCandi):
    Candi_Termahal = HargaCandi(CandiData, 1)
    id_termahal = 1
    for i in range (1, BarisCandi):
        if Candi_Termahal < HargaCandi(CandiData, i):
            Candi_Termahal = HargaCandi(CandiData, i)
            id_termahal = i
    if hitungIsi(CandiData, BarisCandi) > 0:
        print("ID Candi Termahal:", id_termahal, f"(Rp {Candi_Termahal})")
    else:
        print("ID Candi Termahal: -")
    
# Menentukan Candi Termurah yang bukan 0
def CandiTermurah(CandiData, BarisCandi):
    Candi_Termurah = HargaCandi(CandiData, 1)
    id_termurah = 1
    for i in range (1, BarisCandi):
        if HargaCandi(CandiData, i) > 0:
            if Candi_Termurah > HargaCandi(CandiData, i):
                Candi_Termurah = HargaCandi(CandiData, i)
                id_termurah = i
    if hitungIsi(CandiData, BarisCandi) > 0:
        print("ID Candi Termurah:", id_termurah, f"(Rp {Candi_Termurah})")
    else:
        print("ID Candi Termurah: -")


def AmbilLaporanCandi(CandiData, BarisCandi):
    print("Total Candi:", hitungIsi(CandiData, BarisCandi))
    Material(CandiData, BarisCandi)
    CandiTermahal(CandiData, BarisCandi)
    CandiTermurah(CandiData, BarisCandi)