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
    OldUserInfo = UserInfo
    #getAuthInfo
    auth = memintaAutentikasi()
    print()
    
    # Cari Username
    for i in range(1,103):
      if UserData[i][0] == auth[0]:
        UserInfo[0] = True
        UserInfo[1] = UserData[i][0]
        UserInfo[2] = UserData[i][1]
        UserInfo[3] = UserData[i][2]
        break

      # DEBUG
      #print(UserInfo)      
    
    if UserInfo[0] == False:
      print("Username tidak ditemukan.")
      return OldUserInfo
    else:
      if auth[1] == UserInfo[2]:
        print("login sukses")
        return UserInfo
    
    
  else:
    print("Login gagal!")
    print("Anda telah login dengan username",UserInfo[1]+",",'silahkan lakukan "logout" sebelum melakukan login kembali.')
    return OldUserInfo
  
# Debug
#UserData = [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
#UserInfo = [False, "", "", ""]

#print(login(UserInfo,UserData))