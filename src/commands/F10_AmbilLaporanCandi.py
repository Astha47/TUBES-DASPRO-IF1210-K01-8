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
def Material(DaftarCandi, Nmax):
    Total_Pasir = 0
    Total_Batu = 0
    Total_Air = 0
    for i in range (Nmax):
        Total_Pasir = Total_Pasir + DaftarCandi[i].pasir
        Total_Batu = Total_Batu + DaftarCandi[i].batu
        Total_Air = Total_Air + DaftarCandi[i].air
    print("Total_Pasir :" , Total_Pasir)
    print("Total_Batu :" , Total_Batu)
    print("Total_Air :" , Total_Air)


def TotalCandi(DaftarCandi):
    Total_Candi = 0
    for i in range (Nmax):
        if DaftarCandi[i].pasir > 0 or Candi[i].batu > 0 or DaftarCandi[i].air > 0:
            Total_Candi = Total_Candi + 1
    return(Total_Candi)


def HargaCandi(DaftarCandi):
    return(10000*DaftarCandi.pasir + 15000*DaftarCandi.batu + 7500*DaftarCandi.air)


def CandiTermahal(DaftarCandi, Nmax):
    Candi_Termahal = DaftarCandi[0]
    for i in range (1, Nmax):
        if HargaCandi(Candi_Termahal) < HargaCandi(DaftarCandi[i]):
            Candi_Termahal = DaftarCandi[i]
    return(Candi_Termahal.id)
    

def CandiTermurah(DaftarCandi, Nmax):
    Candi_Termurah = DaftarCandi[0]
    for i in range (1, Nmax):
        if HargaCandi(Candi_Termurah) > HargaCandi(DaftarCandi[i]):
            Candi_Termurah = DaftarCandi[i]
    return(Candi_Termurah.id)


def AmbilLaporanCandi(DaftarCandi, Nmax):
    print("Total Candi:", TotalCandi(DaftarCandi))
    Material(DaftarCandi, Nmax)
    print("ID Candi Termahal:", CandiTermahal(DaftarCandi, Nmax), f"(Rp {HargaCandi(DaftarCandi[CandiTermahal(DaftarCandi, Nmax)])})")
    print("ID Candi Termurah:", CandiTermurah(DaftarCandi, Nmax), f"(Rp {HargaCandi(DaftarCandi[CandiTermurah(DaftarCandi, Nmax)])})")

# CONTOH APLIKASI

"""
DaftarCandi[0].id = 0
DaftarCandi[0].pasir = 1
DaftarCandi[0].batu = 2
DaftarCandi[0].air = 3

DaftarCandi[1].id = 1
DaftarCandi[1].pasir = 2
DaftarCandi[1].batu = 3
DaftarCandi[1].air = 4

DaftarCandi[2].id = 2
DaftarCandi[2].pasir = 5
DaftarCandi[2].batu = 6
DaftarCandi[2].air = 7


AmbilLaporanCandi(DaftarCandi, 3)

"""


