numero = 21

if numero != 0:
    vecchio = 1
    nuovo = 1
    for i in range(numero - 1):
        tmp = nuovo
        nuovo = vecchio
        vecchio = vecchio + tmp
    print(nuovo)
else:
    print(0)