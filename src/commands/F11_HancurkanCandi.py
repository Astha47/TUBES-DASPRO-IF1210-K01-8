def idFinder(CandiData, BarisCandi, id):
    data = [False,0]
    for i in range(1, BarisCandi):
        if CandiData[i][0] == id:
            data = [True, i]
            break
    return data

def getaction(id):
    action = input('Apakah anda yakin ingin menghancurkan candi ID: '+id+' (Y/N)? ')

    if action == 'y' or action == 'Y' or action == 'n' or action == 'N':
        return action
    else:
        print('Opsi tidak valid')
        return getaction(id)

def hancurkancandi(CandiData, BarisCandi):
    id = input('Masukkan ID candi: ')

    data = idFinder(CandiData, BarisCandi, id)

    if data[0]:
        action = getaction(id)
        if action == 'y' or action == 'Y':
            CandiData[data[1]] = ['','','','','']
            print()
            print('Candi telah berhasil dihancurkan.')
    else:
        print('Tidak ada candi dengan ID tersebut.')

    return CandiData