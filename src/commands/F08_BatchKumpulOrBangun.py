#import random
import src.commands.B01_RNG as RNG

def hitungJin(UserData, BarisUser, Tipe):
    jumlah = 0

    for i in range(1,BarisUser):
        if UserData[i][2] == Tipe:
            jumlah +=1
    
    return jumlah

def hitungKosong(CandiData, BarisCandi):
    jumlah = 0
    for i in range(1, BarisCandi):
        if CandiData[i][0] == '':
            jumlah += 1
    return jumlah

def batchkumpul(BahanBangunanData, UserData, BarisUser):
    Tipe = 'Pengumpul'
    jumlah = hitungJin(UserData, BarisUser, Tipe)

    if jumlah > 0:
        pasir = 0
        batu = 0
        air = 0

        for i in range(jumlah):
            pasir += RNG.RNG(5) 
            batu += RNG.RNG(5)
            air += RNG.RNG(5)
        
        print('Mengerahkan',jumlah,'jin untuk mengumpulkan bahan.')
        print('Jin menemukan total',pasir,'pasir,',batu,'batu, dan',air,'air.')

        # Tulis data
        # Proses Data Awal
        pasirAwal = int(BahanBangunanData[1][2])
        batuAwal  = int(BahanBangunanData[2][2])
        airAwal   = int(BahanBangunanData[3][2])

        pasir += pasirAwal
        batu  += batuAwal
        air   += airAwal

        BahanBangunanData[1][2] = str(pasir)
        BahanBangunanData[2][2] = str(batu)
        BahanBangunanData[3][2] = str(air)

    else:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')

    return BahanBangunanData


def batchbangun(CandiData, UserData, BarisCandi, BarisUser, BahanBangunanData):
    Tipe = 'Pembangun'
    jumlah = hitungJin(UserData, BarisUser, Tipe)

    if jumlah>0:
        
        matriksbangun = [[0,0,0,0,0] for i in range(jumlah)]

        # isi ID
        for i in range(jumlah):
            for j in range(1,101):
                Found = False
                for i in range(1,BarisCandi):
                    if CandiData[i][0] == j:
                        Found = True
                        break

                if Found == False:
                    for i in range(jumlah):
                        if matriksbangun[i][0] == j:
                            Found = True
                            break
                if Found == False:
                    matriksbangun[i][0] = j
                    break
        
        # isi ID Jin
        iterator = 0
        for i in range(1,BarisUser):
            if UserData[i][2] == Tipe:
                matriksbangun[iterator][1] == UserData[i][0]
                iterator +=1
            if iterator == jumlah:
                break

                
        
        pasir  = 0
        batu   = 0
        air    = 0

        # Isi data material
        for i in range(jumlah):
            pasirbaru = RNG.RNGnoNull(5)
            pasir += pasirbaru
            batubaru = RNG.RNGnoNull(5)
            batu += batubaru
            airbaru = RNG.RNGnoNull(5)
            air += airbaru

            matriksbangun[i][2] = pasirbaru
            matriksbangun[i][3] = batubaru
            matriksbangun[i][4] = airbaru
        
        # Dapatkan data bahan bangunan
        stokpasir = int(BahanBangunanData[1][2])
        stokbatu  = int(BahanBangunanData[2][2])
        stokair   = int(BahanBangunanData[3][2])

        print('Mengerahkan',jumlah,'jin untuk membangun candi dengan total bahan',pasir,'pasir,',batu,'batu, dan',air,'air.')

        if pasir <= stokpasir and batu <= stokbatu and air <= stokair:

            # Modifikasi Jumlah bahan bangunan
            BahanBangunanData[1][2] = str(stokpasir - pasir)
            BahanBangunanData[2][2] = str(stokbatu - batu)
            BahanBangunanData[3][2] = str(stokair - air)


            # Hitung jumlah slot kosong
            jumlahKosong = hitungKosong(CandiData, BarisCandi)
            if jumlah <= jumlahKosong:
                for i in range(jumlah):
                    for j in range(1,BarisCandi):
                        if CandiData[j][0] == '':
                            CandiData[j] = matriksbangun[i]
                            break
                print("Jin berhasil membangun total",jumlah,"candi.")
            else:
                for i in range(jumlahKosong):
                    for j in range(1,BarisCandi):
                        if CandiData[j][0] == '':
                            CandiData[j] = matriksbangun[i]
                            break
                print("Jin berhasil membangun total",jumlahKosong,"candi.")
            
        else:
            # hitung kekurangan
            kurangPasir = pasir - stokpasir
            kurangBatu  = batu - stokbatu
            kurangAir   = air - stokair

            if kurangPasir < 0:
                kurangPasir = 0
            
            if kurangBatu < 0:
                kurangBatu = 0
            
            if kurangAir < 0:
                kurangAir = 0

            print('Bangun gagal. Kurang',end='')
            if kurangPasir > 0 and kurangBatu == 0 and kurangAir == 0:
                print(kurangPasir,'pasir.')
            elif kurangPasir == 0 and kurangBatu > 0 and kurangAir == 0:
                print(kurangBatu,'batu.')
            elif kurangPasir == 0 and kurangBatu == 0 and kurangAir > 0:
                print(kurangAir,'air.')
            elif kurangPasir > 0 and kurangBatu > 0 and kurangAir == 0:
                print(kurangPasir,'pasir, dan',kurangBatu,'batu.')
            elif kurangPasir > 0 and kurangBatu == 0 and kurangAir > 0:
                print(kurangPasir,'pasir, dan',kurangAir,'air.')
            elif kurangPasir == 0 and kurangBatu > 0 and kurangAir > 0:
                print(kurangBatu,'batu, dan',kurangAir,'air.')
            elif kurangPasir > 0 and kurangBatu > 0 and kurangAir > 0:
                print(kurangPasir,'pasir,',kurangBatu,'batu, dan',kurangAir,'air.')
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')

    return [UserData, CandiData, BahanBangunanData]