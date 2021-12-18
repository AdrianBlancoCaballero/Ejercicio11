# Ejercicio 11

import bubble_sort as bs

while True:
    lista = []
    fin = False


    while True:
        while True:
            numero = input("Introduzca el número deseado: ")
            if numero == "fin":
                fin = True
                break
            try:
                numero = int(numero)
                break
            except:
                print("El dato intrducido no es un número.")

        if fin or numero == -9999:
            break
        lista.append(numero)
    if fin:
        break

    lo = bs.BubbleSort(lista)
    print("Lista introducida, ordenada: ", "\n", lo.sorted_list)
