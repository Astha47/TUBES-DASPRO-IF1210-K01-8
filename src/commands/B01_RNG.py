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

# DEBUG
#for i in range(12):
#    print(RNG(25))