def multiplicacion(n, m):
    if m == 0:
        return 0
    return n + multiplicacion(n, m - 1)

print (multiplicacion(5, 4)) 