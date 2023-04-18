# IMPORT MODULE
import argparse
import os
import time

# IMPORT FUNCTIONS
import src.commands.F01_Login                   as F01
import src.commands.F02_Logout                  as F02
import src.commands.F03_SummonJin               as F03
import src.commands.F04_HilangkanJin            as F04
import src.commands.F05_UbahTipeJin             as F05
import src.commands.F06_JinPembangun            as F06
import src.commands.F07_JinPengumpul            as F07
import src.commands.F08_BatchKumpulOrBangun     as F08
import src.commands.F09_AmbilLaporanJin         as F09
import src.commands.F10_AmbilLaporanCandi       as F10
import src.commands.F11_HancurkanCandi          as F11
import src.commands.F12_AyamBerkokok            as F12
import src.commands.F13_Load                    as F13
import src.commands.F14_Save                    as F14
import src.commands.F15_Help                    as F15
import src.commands.F16_Exit                    as F16

# DEFINISI DAN SPESIFIKASI VARIABEL GLOBAL
"""
UserActive : {  loginsession : Boolean {Menentukan apakah ada akun yang melakukan login}
                username     : String
                password     : String
                role         : String }
User       : Array of  {  username     : String
                          password     : String
                          role         : String }

UserInfo        : UserActive  = Berfungsi sebagai variabel penentu useraccount yang login
MainDirectory   : String      = Berfungsi sebagai penentu lokasi data yang digunakan
UserData        : User        = Data utama autentikasi login
"""

# INISIALISASI
UserInfo = [False, "", "", ""]
Run = False

# PARSER
parser = argparse.ArgumentParser()
parser.add_argument("SaveGame", nargs="?", default="",help="Nama dari direktori penyimpanan sesi")
args = parser.parse_args()

if args.SaveGame: 
  if (os.path.exists('src/SaveGame/'+args.SaveGame)):
    os.system('cls')
    print("Loading...")
    MainDirectory = 'src/SaveGame/'+args.SaveGame

    # LOADING GLOBAL DATA

    # PERHATIANN!!!
    """
    Bentuk data UserData, CandiData, dan BahanBangunan Data akan berbentuk sama persis seperti
    tabel pada file csv dengan indeks baris pertama adalah header (header masuk dalam baris)
    """


    # Data Jumlah Baris dan Kolom
    BarisUser = 104
    KolomUser = 3
    BarisCandi = 101
    KolomCandi = 5
    BarisBBangunan = 101
    KolomBBangunan = 3

    UserData = F13.load(MainDirectory+"/user.csv", BarisUser, KolomUser) # Matrix
    CandiData = F13.load(MainDirectory+"/candi.csv", BarisCandi, KolomCandi) # Matrix
    BahanBangunanData = F13.load(MainDirectory+"/bahan_bangunan.csv", BarisBBangunan, KolomBBangunan) # Matrix
    Run = True

    # PERHATIAN
    """
    Seluruh data diatas berbentuk matriks dan untuk baris ke-0 untuk tiap data merupakan Header dari file CSV
    Harap ini diperhatikan untuk setiap iterasi untuk menghindari fatal error
    """

    # DEBUG
    #print('Userdata = ',UserData)
    #print('CandiData = ', CandiData)
    #print('BahanBangunanData = ',BahanBangunanData)
    #debug = input()


    time.sleep(1)
    os.system('cls')


    # DEBUG
    #print(UserData)
    #print(CandiData)
    #print(BahanBangunanData)


    print("Selamat datang di program “Manajerial Candi”\nSilahkan masukkan username Anda")
    UserInfo = F01.login(UserInfo, UserData)
  else:
    print('Folder "'+args.SaveGame+'" tidak ditemukan.')
else:
  print("Tidak ada nama folder yang diberikan!")
  print()
  print("Usage: python main.py <nama_folder>")


while Run:
  command = input()

  if command == "login":
    UserInfo = F01.login(UserInfo,UserData)
  elif command == "logout":
    UserInfo = F02.logout(UserInfo)
  elif command == "summonjin":
    F03.summonjin()
  elif command == "hapusjin":
    F04.hapusjin()
  elif command == "ubahjin":
    F05.ubahjin()
  elif command == "bangun":
    F06.bangun()
  elif command == "kumpul":
    F07.kumpul()
  elif command == "batchkumpul":
    F08.batchkumpul
  elif command == "laporanjin":
    F09.laporanjin()
  elif command == "laporancandi":
    F10.laporancandi()
  elif command == "hancurkancandi":
    F11.hancurkancandi()
  elif command == "ayamberkokok":
    F12.ayamberkokok()
  elif command == "save":
    F14.save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)
  elif command == "help":
    F15.help(UserInfo)
  elif command == "exit":
    F16.exit()
  else:
    print("Command yang anda masukkan salah!")
    print('gunakan "help" untuk menampilkan petunjuk')
