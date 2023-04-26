print("Esta es la lista de nombres impresas por un for")

listaNombres = ["Manzana", "pera", "Guayaba", "Fresa", "Mora"]
for i in range(0, len(listaNombres)):
    print(listaNombres[i])

for i in range(0, len(listaNombres)):
    print("")
    for j in range(0, len(listaNombres[i])):
        print(listaNombres[i][j])
