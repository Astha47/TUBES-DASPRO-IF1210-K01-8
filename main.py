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
import src.toolkit.B05_UndoStep                  as B05
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
UserDataCache = [[],3]
CandiDataCache = [[],5]
BahanBangunanDataCache = [[],3]
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

    DataSementara = F03.summonjin(UserData, BarisUser)
    
    if DataSementara[0]:
      UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      cacheIndex += 1
      UserData = DataSementara[1]
      

  elif command == "hapusjin" and UserInfo[3] == 'bandung_bondowoso':

    # Aksi prosedural multivariable

    aksi = F04.hapusjin(UserData, BarisUser)
    if aksi[0]:

      UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      cacheIndex += 1

      #Delete User Jin
      UserData[aksi[1]] = ['','','']
      #Delete Candi yang Dibangun Jin
      for i in range(1,BarisCandi):
        if CandiData[i][1] == aksi[2]:
          CandiData[i] = ['','','','','']

  elif command == "ubahjin" and UserInfo[3] == 'bandung_bondowoso':

     DataSementara =F05.ubahjin(UserData, BarisUser)
     if DataSementara[0]:
       
        UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
        CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
        BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
        cacheIndex += 1
       
        UserData = DataSementara[1]

  elif command == "bangun" and UserInfo[3] == 'Pembangun':

    data = F06.bangun(CandiData, BahanBangunanData, BarisCandi, UserInfo[3])
    
    if data[2]:

      UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      cacheIndex += 1

      CandiData = data[0]
      BahanBangunanData = data[1]
      #print("Candi :",CandiData)
      #print("Bahan Bangunan :",BahanBangunanData)
    
  elif command == "kumpul" and UserInfo[3] == 'Pengumpul':

    UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
    CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
    BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
    cacheIndex += 1

    BahanBangunanData = F07.kumpul(BahanBangunanData)

  elif command == "batchkumpul" and UserInfo[3] == 'bandung_bondowoso':

    DataSementara = F08.batchkumpul(BahanBangunanData, UserData, BarisUser)
    if DataSementara[0]:
      UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      cacheIndex += 1
      BahanBangunanData = DataSementara[1]

  elif command == "batchbangun" and UserInfo[3] == 'bandung_bondowoso':

    data = F08.batchbangun(CandiData, UserData, BarisCandi, BarisUser, BahanBangunanData)
    UserData            = data[0]
    CandiData           = data[1]
    BahanBangunanData   = data[2]

  elif command == "laporanjin" and UserInfo[3] == 'bandung_bondowoso':

    F09.ambillaporanjin(UserData, BarisUser, BahanBangunanData, CandiData, BarisCandi)

  elif command == "laporancandi" and UserInfo[3] == 'bandung_bondowoso':

    F10.AmbilLaporanCandi(CandiData, BarisCandi)

  elif command == "hancurkancandi" and UserInfo[3] == 'roro_jonggrang':

    CandiData = F11.hancurkancandi(CandiData, BarisCandi)

  elif command == "ayamberkokok" and UserInfo[3] == 'roro_jonggrang':

    F12.ayamberkokok(CandiData, BarisCandi)
    
  elif command == "save"and UserInfo[0] == True:

    F14.save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)

  elif command == "help":

    F15.help(UserInfo)

  elif command == "exit":

    Run = F16.exit(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)

  #elif command == "undo":
  #elif command == "savecache":
    #UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
    #CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
    #BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
    #cacheIndex += 1
    
  elif command == "undostep":
    if cacheIndex < 1:
      print("Tidak ada langkah sebelum kondisi saat ini!")
    else:
      BahanBangunanDataProcess = B05.undostep(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      BahanBangunanData = BahanBangunanDataProcess[0]
      BahanBangunanDataCache = BahanBangunanDataProcess[1]
      cacheIndex += -1
      print(BahanBangunanData)
    
  else:
    print("Command yang anda masukkan salah!")
    print('gunakan "help" untuk menampilkan petunjuk')

    #DEBUG
    #print(BahanBangunanData)
    #print(UserData)
    #print(CandiData)
