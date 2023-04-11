# IMPORT MODULE
import argparse
import os

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
import src.commands.F14_Save                    as F16
import src.commands.F15_Help                    as F17
import src.commands.F16_Exit                    as F18

# PARSER
parser = argparse.ArgumentParser()
parser.add_argument("SaveGame", help="Nama dari direktori penyimpanan sesi")
args = parser.parse_args()

if args.SaveGame: 
  if (os.path.exists('src/SaveGame/'+args.SaveGame)):
    MainDirectory = 'src/SaveGame/'+args.SaveGame
    MainData = F13.Load(MainDirectory)
    F01.login()
  else:
    print('Folder "'+args.SaveGame+'" tidak ditemukan.')
else:
  print("Tidak ada nama folder yang diberikan!")
  print()
  print("Usage: python main.py <nama_folder>")


UserInfo = [False, "Null", "Null", "Null"]
while True:
  command = input()

  if command == "Login":
    UserInfo = F01.Login(UserInfo)
  elif :
  elif :
  elif :
  else:
    
