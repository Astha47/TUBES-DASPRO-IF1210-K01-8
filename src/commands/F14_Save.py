def save ():
    a = input("Masukkan nama folder : ")
    if a in os.listdir():
        print("Berhasil menyimpan data di folder", a)
    else :
        os.mkdir(a)
        print("membuat folder", a)
        print("Berhasil menyimpan data di folder", a)