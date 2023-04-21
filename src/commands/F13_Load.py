def load(FileDirectory,baris,kolom):

    # Inisalisasi 
    Array = [["" for i in range(kolom)] for j in range(baris)]

    file = open(FileDirectory, "r")
    RawString = file.read()
    file.close()

    
    # Memisahkan per-line
    jumlahBaris = 1 # Menghitung jumlah baris dalam file terlebih dahulu
    for i in range(len(RawString)):
        if RawString[i] == '\n':
            jumlahBaris += 1
    
    #print("Jumlah baris :", jumlahBaris)

    currentText = ""
    isiperline = [ 0 for i in range(jumlahBaris)]
    pengisian = 0
    for i in range(len(RawString)):
        if RawString[i] == '\n':
            isiperline[pengisian] = currentText
            pengisian += 1
            currentText = ""
        else:
            currentText += RawString[i]
    isiperline[jumlahBaris-1] = currentText
    
    #print("Isi perline :", isiperline)

    # Memisahkan per kolom
    """
    # hitung kolom
    jumlahKolom = 1
    for i in range(len(isiperline[0])):
        print(isiperline[0][i])
        if isiperline[0][i] == ";":
            jumlahKolom += 1
    """
    
    # Masukkan isi Array
    for i in range(jumlahBaris):
        kata = ""
        iterasi = 0
        for j in range(len(isiperline[i])):
            if isiperline[i][j] != ';':
                kata += isiperline[i][j]
            else:
                Array[i][iterasi] = kata
                iterasi +=1
                kata = ""
            Array[i][iterasi] = kata


    return Array

#print(load("src/SaveGame/debug/bahan_bangunan.csv",4,3))