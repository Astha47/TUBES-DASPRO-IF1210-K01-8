import os

def ArrayKeRawString(Array,Kolom,Baris):
    RawString = ''
    for i in range(Baris):
        if Array[i][0] != '':
            for j in range(Kolom-1):
                RawString += Array[i][j]
                RawString += ';'
            RawString += Array[i][Kolom-1]
            RawString += '\n'

    #Potong karakter terakhir
    FinalString = ''
    for i in range(len(RawString)-1):
        FinalString += RawString[i]
    return FinalString

def mintainputfolder():
    a = input("Masukkan nama folder : ")
    if a == '':
        print("Nama folder tidak boleh kosong")
        return mintainputfolder()
    elif a == 'newgame':
        print("Maaf folder tersebut terproteksi")
        return mintainputfolder()
    else:
        return a
    


def save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan):
    parentLocation = 'src/SaveGame'
    
    a = mintainputfolder()

    TargetLocation = parentLocation+'/'+a
    if (os.path.isdir(TargetLocation)) == False:
        print("Membuat folder", a)
        # MEMBUAT SAVE SLOT GAME
        os.mkdir(TargetLocation)        
    
    RAWTextUserData = ArrayKeRawString(UserData,KolomUser,BarisUser)
    RAWTextCandiData = ArrayKeRawString(CandiData,KolomCandi,BarisCandi)
    RAWTextBahanBangunanData = ArrayKeRawString(BahanBangunanData,KolomBBangunan,BarisBBangunan)

    # MENULIS USER.CSV
    # ============================================
    # Inisiasi file
    file = open(TargetLocation+"/user.csv", "w")

    # Menulis isi file
    file.write(RAWTextUserData)

    # Menutup file
    file.close()
    # ============================================

    #MENULIS CANDI.CSV
    # Inisiasi file
    file = open(TargetLocation+"/candi.csv", "w")

    # Menulis isi file
    file.write(RAWTextCandiData)

    # Menutup file
    file.close()
    # ============================================

    #MENULIS BAHAN_BANGUNAN.CSV
    # Inisiasi file
    file = open(TargetLocation+"/bahan_bangunan.csv", "w")

    # Menulis isi file
    file.write(RAWTextBahanBangunanData)

    # Menutup file
    file.close()
    # ============================================

    print("Berhasil menyimpan data di folder", a)
    