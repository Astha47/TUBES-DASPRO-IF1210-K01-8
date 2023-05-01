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
import src.commands.B04_dan_B05_UndoStep        as B05
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


    time.sleep(1)
    os.system('cls')


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

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]

    DataSementara = F03.summonjin(UserData, BarisUser)
    
    if DataSementara[0]:
      UserDataCache = B05.SaveCache(UserDataCache, UserData, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      cacheIndex += 1
      UserData = DataSementara[1]
      

  elif command == "hapusjin" and UserInfo[3] == 'bandung_bondowoso':

    # Aksi prosedural multivariable

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]

    aksi = F04.hapusjin(UserData, BarisUser)
    if aksi[0]:

      UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
      cacheIndex += 1

      #Delete User Jin
      UserData[aksi[1]] = ['','','']
      #Delete Candi yang Dibangun Jin
      for i in range(1,BarisCandi):
        if CandiData[i][1] == aksi[2]:
          CandiData[i] = ['','','','','']

  elif command == "ubahjin" and UserInfo[3] == 'bandung_bondowoso':

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]
     

    DataSementara =F05.ubahjin(UserData, BarisUser)
    if DataSementara[0]:
      
      UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
      cacheIndex += 1
       
      UserData = DataSementara[1]

  elif command == "bangun" and UserInfo[3] == 'Pembangun':

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]

    data = F06.bangun(CandiData, BahanBangunanData, BarisCandi, UserInfo[3])
    
    if data[2]:

      UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
      cacheIndex += 1

      CandiData = data[0]
      BahanBangunanData = data[1]
    
  elif command == "kumpul" and UserInfo[3] == 'Pengumpul':

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]

    UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
    CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
    BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
    cacheIndex += 1

    BahanBangunanData = F07.kumpul(BahanBangunanData)

  elif command == "batchkumpul" and UserInfo[3] == 'bandung_bondowoso':
    
    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]


    DataSementara = F08.batchkumpul(BahanBangunanData, UserData, BarisUser)
    if DataSementara[0]:
      UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
      cacheIndex += 1
      BahanBangunanData = DataSementara[1]

  elif command == "batchbangun" and UserInfo[3] == 'bandung_bondowoso':

    # Definisikan array lama
    UserDataOld = [[0 for i in range(KolomUser)] for i in range(BarisUser)]
    CandiDataOld = [[0 for i in range(KolomCandi)] for i in range(BarisCandi)]
    BahanBangunanDataOld = [[0 for i in range(KolomBBangunan)] for i in range(BarisBBangunan)]

    # Isi array lama
    for i in range(BarisUser):
      for j in range(KolomUser):
        UserDataOld[i][j] = UserData[i][j]

    for i in range(BarisCandi):
      for j in range(KolomCandi):
        CandiDataOld[i][j] = CandiData[i][j]

    for i in range(BarisBBangunan):
      for j in range(KolomBBangunan):
        BahanBangunanDataOld[i][j] = BahanBangunanData[i][j]

    data = F08.batchbangun(CandiData, UserData, BarisCandi, BarisUser, BahanBangunanData)
    if data[3]:
      #print("Data Bahan bangunan awal : ",BahanBangunanData)
      UserDataCache = B05.SaveCache(UserDataCache, UserDataOld, BarisUser, cacheIndex)
      CandiDataCache = B05.SaveCache(CandiDataCache, CandiDataOld, BarisCandi, cacheIndex)
      BahanBangunanDataCache = B05.SaveCache(BahanBangunanDataCache, BahanBangunanDataOld, BarisBBangunan, cacheIndex)
      cacheIndex += 1
      UserData            = data[0]
      CandiData           = data[1]
      BahanBangunanData   = data[2]

  elif command == "laporanjin" and UserInfo[3] == 'bandung_bondowoso':

    F09.ambillaporanjin(UserData, BarisUser, BahanBangunanData, CandiData, BarisCandi)
    print()

  elif command == "laporancandi" and UserInfo[3] == 'bandung_bondowoso':

    F10.AmbilLaporanCandi(CandiData, BarisCandi)
    print()

  elif command == "hancurkancandi" and UserInfo[3] == 'roro_jonggrang':

    RawData = F11.hancurkancandi(CandiData, BarisCandi)

    if RawData[0] == True:
      CandiData = RawData[1]
      UserDataCache = [[],3]
      CandiDataCache = [[],5]
      BahanBangunanDataCache = [[],3]

    print()

  elif command == "ayamberkokok" and UserInfo[3] == 'roro_jonggrang':

    F12.ayamberkokok(CandiData, BarisCandi)
    print()
    
  elif command == "save"and UserInfo[0] == True:

    F14.save(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)
    print()

  elif command == "help":

    F15.help(UserInfo)
    print()

  elif command == "exit":

    Run = F16.exit(UserData,CandiData,BahanBangunanData,BarisUser,KolomUser,BarisCandi,KolomCandi,BarisBBangunan,KolomBBangunan)
    
  elif command == "undo" and UserInfo[3] == 'bandung_bondowoso':
    if cacheIndex < 1:
      print("Tidak ada langkah sebelum kondisi saat ini!")
    else:
      BahanBangunanDataProcess = B05.undostep(BahanBangunanDataCache, BahanBangunanData, BarisBBangunan, cacheIndex)
      BahanBangunanData = BahanBangunanDataProcess[0]
      BahanBangunanDataCache = BahanBangunanDataProcess[1]

      UserDataProcess = B05.undostep(UserDataCache, UserData, BarisUser, cacheIndex)
      UserData = UserDataProcess[0]
      UserDataCache = UserDataProcess[1]

      
      CandiDataProcess = B05.undostep(CandiDataCache, CandiData, BarisCandi, cacheIndex)
      CandiData = CandiDataProcess[0]
      CandiDataCache = CandiDataProcess[1]
        

      cacheIndex += -1

      print("Undo sukses!")
      print()
  
  elif (command == "summonjin" or command == "hapusjin" or command == "ubahjin" or command == "bangun" or command == "kumpul" or command == 'batchkumpul' or command == "laporanjin" or command == "laporancandi" or command == 'hancurkancandi' or command == "ayamberkokok" or command == "save") and UserInfo[0] == False:
    print("Anda belum melakukan login, silakan login trlrbih dahulu!")
  else:
    print("Command yang anda masukkan salah!")
    print('gunakan "help" untuk menampilkan petunjuk')