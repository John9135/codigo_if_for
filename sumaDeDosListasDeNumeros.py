listaDeNumeros1 = []
listaDeNumeros2 = []
listaDeSuma = []

print("Ingrese 5 números para la primera lista")
for i in range(0, 5):
    listaDeNumeros1.append(input("Ingrese un número: "))

print("Ingrese 5 números para la segunda lista")
for i in range(0, 5):
    listaDeNumeros2.append(input("Ingrese un número: "))

for i in range(0, 5):
    listaDeSuma.append(int(listaDeNumeros1[i]) + int(listaDeNumeros2[i]))
    print("La suma de los números de la lista en la misma posición es: "
          + str(listaDeSuma[i]))
