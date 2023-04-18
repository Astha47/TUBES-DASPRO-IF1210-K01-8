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
    masukan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if (masukan == "y" or masukan == "Y"):
        #save()
        Run = False
    elif (masukan == "n" or masukan == "N"):
        Run = False
    while (masukan != "y" or masukan != "Y" or masukan != "n" or masukan != "N"):
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    return Run




