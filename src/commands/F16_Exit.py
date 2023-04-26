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
import src.commands.F14_Save as F14

def exit(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan):
    masukan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if (masukan == "y" or masukan == "Y"):
        F14.save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)
        Run = False
    elif (masukan == "n" or masukan == "N"):
        Run = False
    else:
        Run = exit()
    return Run



"""
#NOTAL

PROGRAM Exit
{spesifikasi : Keluar dari program dengan pilihan save atau tidak}
{import fungsi F14_Save as F14}

KAMUS
masukan : string

function exit(Run : boolean) -> boolean
{fungsi ini akan menampilkan pesan apakah user ingin melakukan penyimpanan file sebelum keluar dari program lalu mengakhiri program dan keluar dari program}

ALGORITMA
    input (masukan)
    if (masukan == "y" or masukan == "Y") then
        F14.save()
        Run <- false
    else if (masukan == "n" or masukan == "N") then
        Run <- false
    else
        exit()
    -> Run
"""
