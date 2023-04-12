def loadCSV(FileDirectory,baris,kolom):

    # Inisalisasi 
    Array = [["" for i in range(kolom)] for j in range(baris)]

    file = open(FileDirectory, "r")
    RawString = file.read()
    file.close()

    # Memisahkan per-line
    jumlahBaris = 0 # Menghitung jumlah baris dalam file terlebih dahulu
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

    # Memisahkan per kolom
    # hitung semicolon

    nsemicolon = 0
    for i in range(len(isiperline[0])):
        print(isiperline[0][i])
        if isiperline[0][i] == ";":
            nsemicolon += 1
    return Array

loadCSV("",5,3)