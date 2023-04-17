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
def ayamberkokok(JumlahCandi):
    suaraAyam = print("Kukuruyuk.. Kukuruyuk..")
    totalCandi = "Jumlah candi : " + str(JumlahCandi)  
    if JumlahCandi < 100 :
        output = print("Selamat, Roro Jonggrang memenangkan permainan!\n \n*Bandung Bondowoso angry noise*\n \nRoro Jonggrang dikutuk menjadi candi." )
    else :
        output = print("Yah, Bandung Bondowoso memenangkan permainan!")

    return totalCandi





    