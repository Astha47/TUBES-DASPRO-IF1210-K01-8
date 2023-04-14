#def exit():

#F16 - Exit

#SPESIFIKASI DAN DEFINISI
"""
UserActive : {  loginsession : Boolean
                username     : String
                password     : String
                role         : String }
"""

#procedure exit(output Run : Boolean)
#{Prosedur ini akan menampilkan pesan apakah user ingin melakukan penyimpanan file sebelum keluar dari program lalu mengakhiri program dan keluar dari program}

#REALISASI

#procedure exit(output Run : Boolean)
#Kamus Lokal
"""
Run : Boolean
"""
#Algoritma

def exit():
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if (input() == "y" or input() == "Y"):
        F14()
        Run = False
    elif (input() == "n" or input() == "N"):
        Run = False
    else :
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")




