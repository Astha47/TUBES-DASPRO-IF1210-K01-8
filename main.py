# IMPORT MODULE
import argparse
import os

# IMPORT FUNCTIONS
import src.commands.F01_Login
import src.commands.F02
import src.commands.F03
import src.commands.F04
import src.commands.F05
import src.commands.F06
import src.commands.F07
import src.commands.F08
import src.commands.F09
import src.commands.F10
import src.commands.F11
import src.commands.F12
import src.commands.F13
import src.commands.F14
import src.commands.F15
import src.commands.F16

# PARSER
parser = argparse.ArgumentParser()
parser.add_argument("SaveGame", help="Nama dari direktori penyimpanan sesi")
args = parser.parse_args()

if args.SaveGame: 
  if (os.path.exists('src/SaveGame/'+args.SaveGame)):
    MainDirectory = 'src/SaveGame/'+args.SaveGame
    src.commands.F01.login()
  else:
    print('Folder "'+args.SaveGame+'" tidak ditemukan.')
else:
  print("Tidak ada nama folder yang diberikan!")
  print()
  print("Usage: python main.py <nama_folder>")
src.commands.F01.halo()