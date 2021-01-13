a = 4008 
b = 8840

somma = 0
for x in range(a, b+1):
    if x%2:
        somma += x
print(somma)