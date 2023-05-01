def SaveCache(arrayCache, array, barisarray, cacheindex):

    #print('Cache lama', arrayCache)
    #print('Array yang akan dimasukkan : ', array)

    oldarray = arrayCache[0]
    bariscache = cacheindex*barisarray
    kolomcache = arrayCache[1]

    cacheindex += 1
    newbariscache = cacheindex*barisarray

    # Membuat Array Penampungan baru
    newarray = [[0 for i in range(kolomcache)] for i in range(newbariscache)]

    # Mengisikan baris Array dari array lama
    for i in range(bariscache):
        for j in range(kolomcache):
            newarray[i][j] = oldarray[i][j]
    
    cacheindex += 1
    
    # Mengisikan data saat ini
    for i in range(bariscache, newbariscache):
        for j in range(kolomcache):
            newarray[i][j] = array[i-bariscache][j]
    
    output = [newarray, kolomcache]

    # DEBUG
    #print(newarray)

    return output

def undostep(arraycache, arraytarget, barisarray, cacheindex):
    # Mengambil Data
    cache = arraycache[0]
    kolomarray = arraycache[1]

    # DEBUG
    #print("Kolom array : ", kolomarray)

    for i in range(barisarray*(cacheindex-1), barisarray*cacheindex):
        for j in range(kolomarray):
            arraytarget[i-barisarray*(cacheindex-1)][j] = cache[i][j]
    
    # Menghapus cache terbaru

    # buat array

    newarray = [[0 for i in range(kolomarray)] for i in range(barisarray*(cacheindex-1))]

    # isi cache

    for i in range(barisarray*(cacheindex-1)):
        for j in range(kolomarray):
            newarray[i][j] = cache[i][j]

    return [arraytarget, [newarray, kolomarray]]

# Debug

"""arraycache = [[[1,2,3],[1,2,3]],3]
cacheindex = 1
barisData = 2
arraytarget = [[0,0,0],[0,0,0]]

print(undostep(arraycache, arraytarget, barisData, cacheindex))"""