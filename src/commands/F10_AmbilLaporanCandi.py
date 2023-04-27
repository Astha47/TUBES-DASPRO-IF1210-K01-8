# [BELUM SELESAI]
# - Ada beberapa fungsi yang harus disesuaikan dengan F06 - Jin Pembangun #OK asumsi aja dulu ~ Fathur
# - Masih belum tau Nmax dihitung pakai apa #Jumlah baris pada candi.csv yang sudah diimport ke matriks CandiData yang ada di main berjumlah pasti 101 baris, atau supaya aman gunakan variabel BarisCandi yang tersedia di main.py ~ Fathur
# - Belum ditambah validasi akun Bondowoso (Menyusul) #Itu tinggal diubah di main.py, aman ~ Fathur

# Def AmbilLaporanCandi
# F10 - Ambil Laporan Candi
# Fungsi menerima info candi lalu memberikan informasi total candi terbangun, bahan-bahan material yang digunakan, dan ID dari candi termahal dan termurah beserta harganya.

# KAMUS


class Candi :
    id : int
    pasir : int
    batu : int
    air : int

Nmax = 3

DaftarCandi = [Candi() for i in range (0, Nmax)]


# ALGORITMA
def hitungIsi(CandiData, BarisCandi):   # Fungsi dari F06
    isi = 0
    for i in range (1,BarisCandi):
        if CandiData[i][0] != '':
            isi += 1
    return isi

def Material(CandiData, BarisCandi):
    Total_Pasir = 0
    Total_Batu = 0
    Total_Air = 0
    for i in range (BarisCandi):
        Total_Pasir += int(CandiData[i][2])
        Total_Batu  += int(CandiData[i][3])
        Total_Air   += int(CandiData[i][4])
    print("Total_Pasir :" , Total_Pasir)
    print("Total_Batu :" , Total_Batu)
    print("Total_Air :" , Total_Air)


def HargaCandi(CandiData, i):
    return(10000*int(CandiData[i][2]) + 15000*int(CandiData[i][3]) + 7500*int(CandiData[i][4]))


def CandiTermahal(CandiData, BarisCandi):
    Candi_Termahal = HargaCandi(CandiData, 1)
    id_termahal = 1
    for i in range (1, BarisCandi):
        if Candi_Termahal < HargaCandi(CandiData, i):
            Candi_Termahal = HargaCandi(CandiData, i)
            id_termahal = i
    print("ID Candi Termahal:", id_termahal, f"(Rp {Candi_Termahal})")
    

def CandiTermurah(CandiData, BarisCandi):
    Candi_Termurah = HargaCandi(CandiData, 1)
    id_termurah = 1
    for i in range (1, BarisCandi):
        if Candi_Termurah > HargaCandi(CandiData, i):
            Candi_Termurah = HargaCandi(CandiData, i)
            id_termurah = i
    print("ID Candi Termurah:", id_termurah, f"(Rp {Candi_Termurah})")


def AmbilLaporanCandi(CandiData, BarisCandi):
    print("Total Candi:", hitungIsi(CandiData, BarisCandi))
    Material(CandiData, BarisCandi)
    CandiTermahal(CandiData, BarisCandi)
    CandiTermurah(CandiData, BarisCandi)
    

# CONTOH APLIKASI

BarisCandi = 4
CandiData = [[f"{0}" for i in range(5)] for i in range (BarisCandi)]

CandiData[1][2] = "3"
CandiData[1][3] = "2"
CandiData[1][4] = "5"

CandiData[2][2] = "4"
CandiData[2][3] = "3"
CandiData[2][4] = "2"

CandiData[3][2] = "4"
CandiData[3][3] = "7"
CandiData[3][4] = "9"

print(CandiData)

AmbilLaporanCandi(CandiData, BarisCandi)
