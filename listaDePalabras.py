listaPalabras = []
for i in range(0, 5):
    print("Escriba una palabra")
    listaPalabras.append(input())

print("Escriba la letra inicial de las palabras que quiere ver")
letra = input().lower()

for palabra in listaPalabras:
    if letra == palabra[0]:
        print(palabra)
