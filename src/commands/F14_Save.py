import os

def ArrayKeRawString(Array,Kolom,Baris):
    RawString = ''
    for i in range(Baris-1):
        for j in range(Kolom-1):
            RawString += Array[i][j]
            RawString += ';'
        RawString += Array[i][Kolom-1]
        RawString += '\n'
    for k in range(Kolom-1):
            RawString += Array[Baris-1][k]
            RawString += ';'
    RawString += Array[Baris-1][Kolom-1]

    #for debug purpose
    #RawString += '{This line must be the last line}'
    return RawString

#DEBUG
#Array = [['asaad','asdasds','asdasds'],['asaad','asdasds','asdasds'],['asaad','asdasds','asdasds']]
#print(ArrayKeRawString(Array,3,3))


def save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan):
    parentLocation = 'src/SaveGame'
    
    a = input("Masukkan nama folder : ")
    TargetLocation = parentLocation+'/'+a
    if (TargetLocation in os.listdir()) == False:
        print("Membuat folder", a)
        # MEMBUAT SAVE SLOT GAME
        os.mkdir(TargetLocation)
        # MEMBUAT FOLDER CACHE
        os.mkdir(TargetLocation+'/cache')
    
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
    