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
UserActive : {  loginsession : Boolean
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
UserInfo = [False, "Null", "Null", "Null"]

# PARSER
parser = argparse.ArgumentParser()
parser.add_argument("SaveGame", help="Nama dari direktori penyimpanan sesi")
args = parser.parse_args()

if args.SaveGame: 
  if (os.path.exists('src/SaveGame/'+args.SaveGame)):
    os.system('cls')
    print("Loading...")
    MainDirectory = 'src/SaveGame/'+args.SaveGame

    # LOADING GLOBAL DATA
    UserData = F13.load(MainDirectory)
    CandiData = F13.load(MainDirectory)
    BahanBangunanData = F13.load(MainDirectory)

    time.sleep(2)
    os.system('cls')
    print("Selamat datang di program “Manajerial Candi”\nSilahkan masukkan username Anda")
    UserInfo = F01.login(UserInfo)
  else:
    print('Folder "'+args.SaveGame+'" tidak ditemukan.')
else:
  print("Tidak ada nama folder yang diberikan!")
  print()
  print("Usage: python main.py <nama_folder>")
 

while True:
  command = input()

  if command == "login":
    UserInfo = F01.login(UserInfo)
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
    F14.save()
  elif command == "help":
    F15.help()
  elif command == "exit":
    F16.exit()
  else:
    print("Command yang anda masukkan salah!")
    print('gunakan "help" untuk menampilkan petunjuk')
