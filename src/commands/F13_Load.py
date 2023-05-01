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