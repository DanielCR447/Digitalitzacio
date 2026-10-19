text = "Hello World"
text2 = "Hola mon!!!"

comptador = 0

for i in range(min(len(text), len(text2))):
    if text[i] == text2[i]:
        comptador += 1

print("El nombre de caràcters iguals en la mateixa posició és", comptador)