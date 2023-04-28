import time

def isThereEmpty(UserData, BarisUser):
    Empty = False
    for i in range(1, BarisUser):
        if UserData[i][0] == '':
            Empty = True
            break
    return Empty

def findEmpty(UserData, BarisUser):
    index = 0
    for i in range(1, BarisUser):
        if UserData[i][0] == '':
            index = i
            break
    return index

def usernameFinder(UserData, BarisUser, keyword):
    Found = False
    for i in range(1,BarisUser):
        if UserData[i][0] == keyword:
            Found = True
            break
    return Found

def summonjin(UserData, BarisUser):
    Empty = isThereEmpty(UserData, BarisUser)
    Perubahan = False
    
    if Empty:
        # Memberikan perintah pada user
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")

        mintaInput = True
        while mintaInput:
            pilihan  = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            if pilihan == "1" or pilihan == "2":
                mintaInput = False
            else:
                print('Tidak ada jenis jin bernomor "'+pilihan+'"!')

        # Menetapkan role
        if pilihan == "1":
            print('Memilih jin "Pengumpul".')
            role = "Pengumpul"
        else:
            print('Memilih jin "Pembangun".')
            role = "Pembangun"


        # Meminta username yang valid
        validateUsername = True
        newJinUsername = ''
        while validateUsername:
            newJinUsername = input("Masukkan username jin: ")
            Found = usernameFinder(UserData, BarisUser, newJinUsername)
            if Found == False and len(newJinUsername)>0:
                validateUsername = False
            elif Found == True and len(newJinUsername)>0:
                print('Username "'+newJinUsername+'" sudah diambil!')
            elif len(newJinUsername) == 0:
                print("Username tidak boleh kosong!")
        
        # Meminta password yang valid
        validatePassword = True
        newJinPassword = ''
        while validatePassword:         
            newJinPassword = input("Masukkan password jin: ")
            if len(newJinPassword)>= 5 and len(newJinPassword) <= 25:
                validatePassword = False
            else:
                print("Password panjangnya harus 5-25 karakter!")
        print()

        # Menuliskan data jin baru
        target = findEmpty(UserData, BarisUser)
        UserData[target][0] = newJinUsername
        UserData[target][1] = newJinPassword
        UserData[target][2] = role

        # Menampilkan pesan sukses
        print('Mengumpulkan sesajen...')
        time.sleep(1)
        print('Menyerahkan sesajen...')
        time.sleep(1)
        print('Membacakan mantra...')
        time.sleep(1)
        print()
        print('Jin '+newJinUsername+' berhasil dipanggil!')
        
        Perubahan = True


    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

    # Menuliskan pemrosesan
    output = [Perubahan, UserData]
    return output
