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
        print("10. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif userInfo[3] == "roro_jonggrang" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("Untuk menghancurkan candi")
        print("3. ayamberkokok")
        print("Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save")
        print("Untuk menyimpan data permainan")
        print("5. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif userInfo[3] == "Pengumpul" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("Untuk mengumpulkan resource candi")
        print("3. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif userInfo[3] == "Pembangun" :
        print("1. logout")
        print("untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("Untuk membangun candi")
        print("3. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    return 

