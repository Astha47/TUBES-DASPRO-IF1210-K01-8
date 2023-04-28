# F09 - Ambil Laporan Jin
# Fungsi menampilkan Total Jin, Total jin tiap tipenya, mencari dan menampilkan jin termalas dan terajin berdasarkan jumlah candi yang mereka buat, dan bahan material yang tersedia.
# Mungkin di fungsi F06 bisa ditambah data di tiap jin tentang berapa banyak candi yang mereka bangun. supaya kalau candinya hancur kinerja jin ngga terperngaruh (Co. Baris 23)

# KAMUS

# TempAr : array of strings

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

"""
# Aku takeoverdulu yah
def KinerjaJin(UserData, BarisUser):
    Terajin = int(UserData[1][3])
    Termalas = int(UserData[1][3])
    for i in range (1, BarisUser):
        if int(UserData[i][3]) > Terajin:
            Terjain = int(UserData[i][3])
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
"""
def sortingLeksiografis(array,panjang):
    for i in range(panjang):
        for j in range(i+1, panjang):
            if array[i] > array[j]:
                # Tukar posisi elemen jika elemen pada indeks i > elemen pada indeks j
                array[i], array[j] = array[j], array[i]
    return array

def KinerjaParaJin(CandiData, BarisCandi, UserData, BarisUser):
    
    jumlah = 0
    for i in range(1, BarisUser):
        if UserData[i][2] == 'Pembangun':
            jumlah += 1

    Pembangun = [['username', 0] for i in range(jumlah)] # Kolom pertama adalah username dan kolom kedua adalah jumlah

    # input username
    iterator = 0
    for i in range(1, BarisUser):
        if UserData[i][2] == 'Pengumpul':
            Pembangun[iterator][0] = UserData[i][0]
            iterator += 1

    # Hitung candi yang dibangun
    for i in range(jumlah):
        for j in range(1, BarisCandi):
            if Pembangun[i][0] == CandiData[j][1]:
                Pembangun[i][1] += 1
    
    rekorcandi = 0
    for i in range(jumlah):
        if Pembangun[i][1] >= rekorcandi:
            rekorcandi = Pembangun[i][1]

    # Analisa jin teratas
    # sudah pasti lebih dari nol apabila data data tidak kosong
    jumlahTopJin = 0
    for i in range(jumlah):
        if Pembangun[i][1] == rekorcandi:
            jumlahTopJin += 1
    
    # Buat arraynya
    TopJin = [0 for i in range(jumlahTopJin)]

    # Pengisian TopJin
    iterator = 0
    for i in range(jumlah):
        if Pembangun[i][1] == rekorcandi:
            TopJin[iterator] = Pembangun[i][0]
            iterator += 1
    
    # Sorting
    TopJin = sortingLeksiografis(TopJin,jumlahTopJin)

    # Analisa jin terbawah
    rekorcanditerendah = rekorcandi
    for i in range(jumlah):
        if Pembangun[i][1] <= rekorcanditerendah:
            rekorcanditerendah = Pembangun[i][1]
    
    jumlahLowJin = 0
    for i in range(jumlah):
        if Pembangun[i][1] == rekorcandi:
            jumlahLowJin += 1
    
    # Buat arraynya
    LowJin = ['username' for i in range(jumlahLowJin)]

    # Pengisian TopJin
    iterator = 0
    for i in range(jumlah):
        if Pembangun[i][1] == rekorcanditerendah:
            LowJin[iterator] = Pembangun[i][0]
            iterator += 1
    
    # Sorting
    LowJin = sortingLeksiografis(LowJin,jumlahLowJin)

    null = False
    if TopJin[0] == LowJin[0]:
        null = True

    if jumlahTopJin>0 and null == False:
        print('Jin Terajin:',TopJin[0])
        print('Jin Termalas:',LowJin[0])
    else:
        print('Jin Terajin: -')
        print('Jin Termalas: -')
    
    return
    

def ambillaporanjin(UserData, BarisUser, BahanBangunanData, CandiData, BarisCandi):
    TotalJin(UserData, BarisUser)
    #KinerjaJin(UserData, BarisUser)
    KinerjaParaJin(CandiData, BarisCandi, UserData, BarisUser)
    print("Jumlah Pasir:", int(BahanBangunanData[1][2]))
    print("Jumlah Air: ", int(BahanBangunanData[2][2]))
    print("Jumlah Batu: ", int(BahanBangunanData[3][2]))
