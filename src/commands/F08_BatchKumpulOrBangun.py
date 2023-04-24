#import random
import src.commands.B01_RNG as RNG

def hitungJin(UserData, BarisUser, Tipe):
    jumlah = 0

    for i in range(1,BarisUser):
        if UserData[i][2] == Tipe:
            jumlah +=1
    
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

        BahanBangunanData[1][2] += pasir
        BahanBangunanData[2][2] += batu
        BahanBangunanData[3][2] += air

    else:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')

    return BahanBangunanData