#(butuh revisi)
#def help() :
#    info command sesuai role

#F15 - Help
#SPESIFIKASI DAN DEFINISI
#procedure help(input : userInfo output : void)
#{Fungsi ini akan menampilkan informasi command yang dapat digunakan oleh user tergantung role yang dijalankan oleh user}
#KAMUS LOKAL
"""
userInfo : array of string (username, password, role, loginSession) 
"""
#ALGORITMA
def help(userInfo) :
    print("=========== HELP ===========")
    #print(userInfo)
    if userInfo[0] == False :
        print("1.login")
        print ("Untuk masuk menggunakan akun")
        print("2. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif userInfo[3] == "bandung_bondowoso" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("Untuk memanggil jin")
        print("3. hapusjin")
        print("Untuk menghapus jin dan candi yang dibuatnya")
        print("4. ubahjin")
        print("Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("Untuk mengumpulkan resources candi oleh semua tipe jin")
        print("6. batchbangun")
        print("Untuk membangun candi oleh semua tipe jin")
        print("7. laporanjin")
        print("Untuk mengetahui kinerja jin dari laporan")
        print("8. laporancandi")
        print("Untuk mengetahui progress pembangunan candi dari laporan")
        print("9. save")
        print("Untuk menyimpan data permainan")
    elif userInfo[3] == "roro_jonggrang" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("Untuk menghancurkan candi")
        print("3. ayamberkokok")
        print("Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save")
        print("Untuk menyimpan data permainan")
    elif userInfo[3] == "Pengumpul" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("Untuk mengumpulkan resource candi")
    elif userInfo[3] == "Pengumpul" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("Untuk membangun candi")

""" 
#NOTAL
PROGRAM Help
{ Spesifikasi : Menampilkan informasi command yang dapat digunakan oleh user tergantung role yang dijalankan oleh user }

KAMUS
userInfo : array of string (username, password, role, loginSession)

procedure help(input : userInfo output : void)
{ I.S : userInfo terdefinisi, menerima input "help" dari user }
{ F.S : Menampilkan informasi command yang dapat digunakan oleh user tergantung role yang dijalankan oleh user }

ALGORITMA
    output("=========== HELP ===========")
    if (userInfo[0] == False) then
        output("1.login")
        output("Untuk masuk menggunakan akun")
        output("2. exit")
        output("Untuk keluar dari program dan kembali ke terminal")
    else if (userInfo[3] == "bandung_bondowoso") then
        output("1. logout")
        output("untuk keluar dari akun yang digunakan sekarang")
        output("2. summonjin")
        output("Untuk memanggil jin")
        output("3. hapusjin")
        output("Untuk menghapus jin dan candi yang dibuatnya")
        output("4. ubahjin")
        output("Untuk mengubah tipe jin")
        output("5. batchkumpul")
        output("Untuk mengumpulkan resources candi oleh semua tipe jin")
        output("6. batchbangun")
        output("Untuk membangun candi oleh semua tipe jin")
        output("7. laporanjin")
        output("Untuk mengetahui kinerja jin dari laporan")
        output("8. laporancandi")
        output("Untuk mengetahui progress pembangunan candi dari laporan")
        output("9. save")
        output("Untuk menyimpan data permainan")
    else if (userInfo[3] == "roro_jonggrang") then
        output("1. logout")
        output("untuk keluar dari akun yang digunakan sekarang")
        output("2. hancurkancandi")
        output("Untuk menghancurkan candi")
        output("3. ayamberkokok")
        output("Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        output("4. save")
        output("Untuk menyimpan data permainan")
    else if (userInfo[3] == "jin_pengumpul") then
        output("1. logout")
        output("untuk keluar dari akun yang digunakan sekarang")
        output("2. kumpul")
        output("Untuk mengumpulkan resource candi")
    else if (userInfo[3] == "jin_pembangun") then
        output("1. logout")
        output("untuk keluar dari akun yang digunakan sekarang")
        output("2. bangun")
        output("Untuk membangun candi")
    
"""