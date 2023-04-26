import time

def RNG(MAX):
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time.time() * 1000) % m
    x = seed
    for i in range(10):
        x = (a * x + c) % m
    time.sleep(0.2)
    return x % (MAX +1)

def RNGnoNull(MAX):
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time.time() * 1000) % m
    x = seed
    for i in range(10):
        x = (a * x + c) % m
    time.sleep(0.2)

    hasil = x % (MAX +1)

    if hasil == 0 or hasil == False:
        #print("hasil yang di dapat :",hasil," maka melakukan rekursif")
        return RNGnoNull(MAX)
    else:
        return hasil

# DEBUG
#for i in range(1000):
   #print(RNGnoNull(5))