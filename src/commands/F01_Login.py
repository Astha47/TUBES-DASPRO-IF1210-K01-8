#def login(UserInfo):
#    return UserInfo

# F01 - Login

# SPESIFIKASI DAN DEFINISI

"""
UserActive : {  loginsession : Boolean
                username     : String
                password     : String
                role         : String }
"""

# procedure memintaAutentikasi (output auth : list of strings)
# {Prosedur ini dijalankan untuk menerima input username dan password dari user}

# function dapatkanInformasiUser (auth : list of strings) -> AuthData : UserLog
# {fungsi ini akan menerima informasi autentikasi dari user dan mencari data yang sesuai dengan username sama.
#  Apabila ditemukan kecocokan username, makan fungsi akan mengembalikan kondisi bernilai True disusul username, password, dan role.
#  namun bila username tidak ditemukan, fungsi akan mengembalikan kondisi bernilai False, disusul "-" untuk username, password, dan role.}

# REALISASI

# procedure memintaAutentikasi (output auth : list of strings)
# Kamus Lokal
# Algoritma
def memintaAutentikasi():
  username = input("Username : ")
  password = input("Password : ")
  auth = [username,password]
  return auth

# Kamus Lokal
# Algoritma
def login(UserInfo, UserData):
  if UserInfo[0] == False:
    
    #getAuthInfo
    auth = memintaAutentikasi()
    print()
      
    
  else:
    print("Login gagal!")
    print("Anda telah login dengan username",UserInfo[1]+",",'silahkan lakukan "logout" sebelum melakukan login kembali.')
  
  return 0