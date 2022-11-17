def factorijele(n):
    suma = 1
    for s in range(2, n+1):
        suma *= s
        print(suma)
    return suma


print(factorijele(5))
