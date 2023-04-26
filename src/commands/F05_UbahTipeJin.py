# F05 - Ubah Tipe Jin

def cariUsernameJin(UserData, BarisUser, usernameJin):
    data = [False,0,'']
    for i in range(1,BarisUser):
        if UserData[i][0] == usernameJin:
            data = [True,i,UserData[2]]
            break
    return data

def memintaAksi(roleAwal, roleAkhir):
    aksi = input('Jin ini bertipe "'+roleAwal+'". Yakin ingin mengubah ke tipe "'+roleAkhir+'" (Y/N)? ')

    if aksi == 'y' or aksi == 'Y' or aksi == 'N' or aksi == 'n':
        return aksi
    else:
        print('Input tidak valid')
        return memintaAksi(roleAwal, roleAkhir)

def ubahjin(UserData, BarisUser):
    # Meninta Username Jin
    usernameJin = input("Masukkan username jin : ")

    # cari data
    data = cariUsernameJin(UserData, BarisUser, usernameJin)

    if data[0]:

        roleAwal = data[2]
        if roleAwal == 'Pengumpul':
            roleAkhir = 'Pembangun'
        else:
            roleAkhir = 'Pengumpul'

        aksi = memintaAksi

        if aksi == 'y' or aksi == 'Y':
            UserData[data[1]][2] = roleAkhir
    else:
        print()
        print("Tidak ada jin dengan username tersebut.")
        
    return UserData
