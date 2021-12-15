# Ejercicio 11

import bubble_sort

lista = []

while True:
    while True:
        try:
            numero = int(input("Introduzca el número deseado: "))
            break
        except:
            print("El dato intrducido no es un número.")
    if numero == -9999:
        break

    lista.append(numero)

print("Lista introducida, sin ordenar: ", "\n", lista)
print(bubble_sort.BubbleSort.print_info())