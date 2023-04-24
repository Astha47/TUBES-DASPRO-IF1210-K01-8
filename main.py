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
#import src.toolkit.SaveCache                    as SaveCache

# DEFINISI DAN SPESIFIKASI VARIABEL GLOBAL
"""
UserActive      : {  loginsession : Boolean {Menentukan apakah ada akun yang melakukan login}
                     username     : String
                     password     : String
                     role         : String }
User            : Array of  {  username     : String
                               password     : String
                               role         : String }

UserInfo        : UserActive  = Berfungsi sebagai variabel penentu useraccount yang login
MainDirectory   : String      = Berfungsi sebagai penentu lokasi data yang digunakan
UserData        : User        = Data utama autentikasi login

Type   Cache    : { CacheData = Berupa Array yang berisikan rekaman perubahan data UserInfo.
                                Kolom terakhir pada array ini berisi indeks perubahan
                    BarisEff  = Nilai baris efektif dari CacheData
                    KolomEff  = Nilai kolom efektif dari CacheData

UserDataCache           : Cache
CandiDataCache          : Cache
BahanBangunanDataCache  : Cache

UndoDump : {  DumpCandi       = Array data candi yang terhapus
              DumpJin         = Array data jin yang terhapus
              NilaiEffDCandi  = Nilai integer }
"""

# INISIALISASI
UserInfo = [False, "", "", ""]
Run = False
UserDataCache = [[[]],0,3]
CandiDataCache = [[[]],0,5]
BahanBangunanDataCache = [[[]],0,3]
cacheIndex = 0

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
    BarisUser = 103
    KolomUser = 3
    BarisCandi = 10001
    KolomCandi = 5
    BarisBBangunan = 4
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
  elif command == "summonjin" and UserInfo[3] == 'bandung_bondowoso':
    UserData = F03.summonjin(UserData, BarisUser)
  elif command == "hapusjin":

    # Aksi prosedural multivariable

    aksi = F04.hapusjin(UserData, BarisUser)
    if aksi[0]:
      #Delete User Jin
      UserData[aksi[1]] = ['','','']
      #Delete Candi yang Dibangun Jin
      for i in range(1,BarisCandi):
        if CandiData[i][1] == aksi[2]:
          CandiData[i] = ['','','','','']

  elif command == "ubahjin":

    UserData = F05.ubahjin(UserData, BarisUser)

  elif command == "bangun":

    data = F06.bangun(CandiData, BahanBangunanData, BarisCandi, UserInfo[3])
    CandiData = data[0]
    BahanBangunanData = data[1]
    
  elif command == "kumpul":

    BahanBangunanData = F07.kumpul(BahanBangunanData)

  elif command == "batchkumpul":

    BahanBangunanData = F08.batchkumpul(BahanBangunanData, UserData, BarisUser)

  elif command == "batchbangun":

    data = F08.batchbangun(CandiData, UserData, BarisCandi, BarisUser, BahanBangunanData)
    UserData            = data[0]
    CandiData           = data[1]
    BahanBangunanData   = data[2]
    
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

    Run = F16.exit(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)

  #elif command == "undo":
    #SaveCache.SaveCache()
  elif command == "undostep":
    print("yahahah belum jadi")
  else:
    print("Command yang anda masukkan salah!")
    print('gunakan "help" untuk menampilkan petunjuk')

    #DEBUG
    print(BahanBangunanData)
    #print(UserData)
    #print(CandiData)
