listaNumeros = []
suma = 0
print ("Escriba la cantidad de número que quiere sumar")
cantidadNumeros = int(input())

for i in range(0, cantidadNumeros):
    print ("Escriba un número")
    listaNumeros.append(int(input()))

for numero in listaNumeros:
    suma += numero

print ("La suma de la lista de números es: " + str(suma))
