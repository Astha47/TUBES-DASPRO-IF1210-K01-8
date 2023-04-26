# Fungsi ini prosedural dan mengoperasikan dua matriks yang beirisan sehingga mengembalikan sebuah matriks kunci

def findJin(UserData, usernameJin, BarisUser):
    Found = False
    index = 0
    for i in range(1,BarisUser):
        if UserData[i][1] == usernameJin:
            Found = True
            index = i
            break
    Finder = [Found,index]
    return Finder

    
def hapusjin(UserData, BarisUser):
    usernameJin = input("Masukkan username jin : ")
    Finder = findJin(UserData, usernameJin, BarisUser)

    if Finder[0]:
        validateAksi = True
        while validateAksi:
            aksi = input("Apakah anda yakin ingin menghapus jin dengan username "+str(usernameJin)+" (Y/N)? ")
            if aksi == "y" or aksi == "Y" or aksi == "n" or aksi == "N":
                validateAksi = False
            else:
                print("Input",aksi,"tidak valid.")
        
        if aksi == "y" or aksi == "Y":
            Index = Finder[1]
            return [True,Index,usernameJin]
        else:
           return [False,'','']

    else:
        print("Tidak ada jin dengan username tersebut.")
        return [False,'','']