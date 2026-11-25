list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

llista_nova = []

for numero in list_num:
    if numero not in llista_nova:
        llista_nova.append(numero)

print("La llista sense duplicats és:", llista_nova)