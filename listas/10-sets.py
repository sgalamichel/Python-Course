# SET -->GRUPO O CONJUNTO - coleccion de datos que no se puede repetir y no esta ordenada.

primer = {1, 1, 2, 2, 3, 4}
# print(primer) #al imprimir vamos a ver que no muestra los elementos duplicados
# PODEMOS TRABAJARLOS AL IGUAL QUE LAS LISTAS.
# primer.add(5)  # agrego elemento
# primer.remove(1)  # elimino elemento
# print(primer)
second = [3, 4, 5]
second = set(second)

# UNION DE LOS SETS QUE LE PASEMOS --> |
print(primer | second)

# INTERSECCION DE SETS --> &
print(primer & second)

# DIFERENCIA --> - (queremos mostrar los datos que se encuentran en el conjunto de la izquierda pero que ademas le estamos quitando los que se encuentran a la derecha)
print(primer - second)

# DIFERENCIA SIMETRICA --> ^ (nos va a devolver los eementos que se encuentren en el primero y en el segundo pero que no se encuentren entre el uno y el otro)
print(primer ^ second)

# NO PODEMOS ACCEDER A LOS SETS, PERO SI PODEMOS PREGUNTAR:
if 5 in second:
    print("Hi!")
