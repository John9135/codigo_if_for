print("Ingrese el número de la tabla que quiere ver")
numero = int(input())

for i in range(1, 11):
    tablaDeMultiplicar = i * numero
    print(str(numero) + " * " + str(i) + " = " + str(tablaDeMultiplicar))
