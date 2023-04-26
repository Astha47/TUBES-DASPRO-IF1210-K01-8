# Fungsi ini melakukan perubahan pada dua matrik, return bernilai tuple kedua matriks tersebut

import src.commands.B01_RNG as RNG

def hitungIsi(CandiData, BarisCandi):
    isi = 0
    for i in range (1,BarisCandi):
        if CandiData[i][0] != '':
            isi += 1
    return isi

def CariIDKosong(CandiData, BarisCandi):
    IDcandi = 0
    for i in range (1,100):
        IDFound = False
        for j in range (1,BarisCandi):
            if i == CandiData[j][0]:
                IDFound = True
                break
        if IDFound == False:
            IDcandi = str(i)
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

    stokpasir = int(BahanBangunanData[1][2])
    stokbatu  = int(BahanBangunanData[2][2])
    stokair   = int(BahanBangunanData[3][2])

    if butuhpasir <= stokpasir and butuhbatu <= stokbatu and butuhair <= stokair:
        

        sisapasir = stokpasir - butuhpasir
        sisabatu  = stokbatu - butuhbatu
        sisaair   = stokair - butuhair

        isi = hitungIsi(CandiData, BarisCandi)

        if  isi < 100:
            # Masukkan ke matriks
            BahanBangunanData[1][2] = str(sisapasir)
            BahanBangunanData[2][2] = str(sisabatu)
            BahanBangunanData[3][2] = str(sisaair)
            IDcandi = CariIDKosong(CandiData, BarisCandi)
            index = CariBarisKosong(CandiData, BarisCandi)

            CandiData[index] = [str(IDcandi), UserJin, str(butuhpasir), str(butuhbatu), str(butuhair)]

        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: "+str(100-isi)+".")

    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

    return [CandiData,BahanBangunanData]
