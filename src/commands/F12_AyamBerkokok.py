#((butuh revisi))

#def ayamberkokok():
#    return suaraAyam, totalCandi, output

# F12 - Ayam Berkokok

# SPESIFIKASI DAN DEFINISI

# function ayamberkokok () -> suaraAyam, totalCandi, output : string
# {fungsi ini akan menghasilkan suara ayam, jumlah candi yang telah dibangun, dan output antara menang atau kalah berdasarkan jumlah candi yang telah dibangun}

# REALISASI

#function ayamberkokok () -> suaraAyam, totalCandi, output : string
#Kamus Lokal
"""
JumlahCandi : integer
suaraAyam : string
totalCandi : string
output : string
"""
#Algoritma
def hitungjumlah(CandiData, BarisCandi):
    jumlah = 0
    for i in range(1, BarisCandi):
        if CandiData[i][0] != '':
            jumlah += 1
    return jumlah


def ayamberkokok(CandiData, BarisCandi):
    JumlahCandi = hitungjumlah(CandiData, BarisCandi)
    print("Kukuruyuk.. Kukuruyuk..\n")
    totalCandi = "Jumlah candi : " + str(JumlahCandi)  
    if JumlahCandi < 100 :
        hasil = print(totalCandi, " \nSelamat, Roro Jonggrang memenangkan permainan!\n \n*Bandung Bondowoso angry noise*\n\nRoro Jonggrang dikutuk menjadi candi." )
    else :
        hasil = print(totalCandi, " \nYah, Bandung Bondowoso memenangkan permainan!")
    return hasil



