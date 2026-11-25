# Crear i mostrar una llista
numeros = [1, 2, 3, 4, 5]
print("Llista de números:", numeros)


# Accedir a elements
noms = ["Anna", "Marc", "Júlia", "Pau"]

print("Primer nom:", noms[0])
print("Últim nom:", noms[len(noms) - 1])


# Afegir i eliminar elements
fruites = ["Poma", "Plàtan", "Taronja"]

fruites.append("Maduixa")  # Afegir un element al final
fruites.pop(0)             # Eliminar el primer element

print("Llista de fruites:", fruites)


# Longitud d'una llista
print("Nombre de números:", len(numeros))
print("Nombre de noms:", len(noms))
print("Nombre de fruites:", len(fruites))