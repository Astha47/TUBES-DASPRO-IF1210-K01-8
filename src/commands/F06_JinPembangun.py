# Fungsi ini melakukan perubahan pada dua matrik, return bernilai tuple kedua matriks tersebut

import src.commands.B01_RNG as RNG

def hitungKosong(CandiData, BarisCandi):
    kosong = 0
    for i in range (1,BarisCandi):
        if CandiData[i][0] == '':
            kosong += 1
    return kosong

def CariIDKosong(CandiData, BarisCandi):
    IDcandi = 0
    for i in range (1,100):
        IDFound = False
        for j in range (1,BarisCandi):
            if i == CandiData[j][0]:
                IDFound = True
                break
        if IDFound == False:
            IDcandi = i
            break
    return IDcandi

def CariBarisKosong(CandiData, BarisCandi):
    index = 0
    for i in range (1,BarisCandi):
        if CandiData[i][0] == '':
            index = i
            break
    return index

def bangun(CandiData, BahanBangunanData, BarisCandi, UserJin):
    butuhpasir = RNG.RNGnoNull(5)
    butuhbatu  = RNG.RNGnoNull(5)
    butuhair   = RNG.RNGnoNull(5)

    stokpasir = BahanBangunanData[1][2]
    stokbatu  = BahanBangunanData[2][2]
    stokair   = BahanBangunanData[3][2]

    if butuhpasir <= stokpasir and butuhbatu <= stokbatu and butuhair <= stokair:
        kosong = hitungKosong(CandiData, BarisCandi)

        sisapasir = stokpasir - butuhpasir
        sisabatu  = stokbatu - butuhbatu
        sisaair   = stokair - butuhair

        # Masukkan ke matriks
        BahanBangunanData[1][2] = sisapasir
        BahanBangunanData[2][2] = sisabatu
        BahanBangunanData[3][2] = sisaair   

        print("Candi berhasil dibangun.")

        if kosong > 0:
            IDcandi = CariIDKosong(CandiData, BarisCandi)
            index = CariBarisKosong(CandiData, BarisCandi)

            CandiData[index] = [IDcandi, UserJin, butuhpasir, butuhbatu, butuhair]
        
        print("Sisa candi yang perlu dibangun: "+str(kosong)+".")

    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

    return [CandiData,BahanBangunanData]
