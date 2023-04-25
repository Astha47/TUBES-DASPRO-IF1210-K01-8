# F09 - Ambil Laporan Jin
# Fungsi menampilkan Total Jin, Total jin tiap tipenya, mencari dan menampilkan jin termalas dan terajin berdasarkan jumlah candi yang mereka buat, dan bahan material yang tersedia.
# Mungkin di fungsi F06 bisa ditambah data di tiap jin tentang berapa banyak candi yang mereka bangun. supaya kalau candinya hancur kinerja jin ngga terperngaruh (Co. Baris 23)

# KAMUS
"
TempAr : array of strings
"
# ALGORITMA

def TotalJin(UserData, BarisUser):
    TotalBangun = 0
    TotalKumpul = 0
    for i in range (1, BarisUser):
        if UserData[i][2] == "Pembangun":
            TotalBangun += 1
        elif UserData[i][2] == "Pengumpul":
            TotalKumpul += 1
    print(f"Total Jin: {TotalBangun + TotalKumpul}")
    print(f"Total Jin Pengumpul: {TotalKumpul}")
    print(f"Total Jin Pembangun: {TotalBangun}")

def KinerjaJin(UserData, BarisUser):
    Terajin = int(UserData[1][3])
    Termalas = int(UserData[1][3])
    for i in range (1, BarisUser):
        if int(UserData[i][3]) > Terajin:
            Terjain = int(Userdata[i][3])
    for j in range (1, BarisUser):
        if int(UserData[j][3]) < Termalas:
            Termalas = int(UserData[j][3])
    First = " "
    for i in range (1, BarisUser):
        if int(UserData[i][3]) == Terajin:
            if First == " ":                            # Mengambil nama terajin pertama.
                First = UserData[i][0]
            else:                                       # Mengurutkan nama terajin berdasarkan alphabet (terendah).
                 TempAr = [First, UserData[i][0]]
                if TempAr[0] < TempAr[1]:
                    First = TempAr[0]
                else:
                    First = TempAr[1]  
    JinTerajin = First
    First = " "
    for i in range (1, BarisUser):
        if int(UserData[i][3]) == Termalas:
            if First == " ":                            # Mengambil nama termalas pertama.
                First = UserData[i][0]
            else:                                       # Mengurutkan nama termalas berdasarkan alphabet (tertinggi).
                TempAr = [First, UserData[i][0]]
                if TempAr[0] > TempAr[1]:
                    First = TempAr[0]
                else:
                    First = TempAr[1]                         
    JinTermalas = First
    print("Jin Terajin: ", JinTerajin)
    print("Jin Termalas: ", JinTermalas)
    

def ambillaporanjin(UserData, BarisUser, BahanBangunanData):
    TotalJin(UserData, BarisUser)
    KinerjaJin(UserData, BarisUser)
    print("Jumlah Pasir:", BahanBangunanData[1][2])
    print("Jumlah Air: ", BahanBangunanData[2][2])
    print("Jumlah Batu: ", BahanBangunanData[3][2])
