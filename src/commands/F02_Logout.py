

def logout(UserInfo):
    if UserInfo[0] == True:
        UserInfo = [False,'','','']
        print('Logout berhasil!')
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
    return UserInfo