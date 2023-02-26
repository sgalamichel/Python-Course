numbers = [2, 8, 9, 6, 45, 28]
# LISTA ORDENADA -->.sort()
# numbers.sort()
# LISTA ORDENADA PERO AL REVES --> .sort(reverse=True)
# numbers.sort(reverse=True)
# A DIFERENCIA DE SORT, devuelve una nueva lista
numbers2 = sorted(numbers)
# SI QUISIERA ESTA NUEVA LISTA PERO AL REVES APLICARIA 'reverse' tambien.
numbers2 = sorted(numbers, reverse=True)

print(numbers)
print(numbers2)

# SI PASAMOS ESTOS DATOS, CON EL INDICE AL COMIENZO SI LO VA A ORDENAR.
# users = [
#     [4, "Ana"],
#     [5, "Jonh"],
#     [22, "Kevin"],
#     [8, "Philliph"],
# ]
# users.sort()

# PERO SI CAMBIAMOS LA UBICACION DEL INDEX NO NOS VA A ORDENAR LA LISTA.
users = [
    ["Ana", 4],
    ["Jonh", 5],
    ["Kevin", 22],
    ["Philliph", 8],
]

# POR LO QUE DEBEMOS PASARLE UNA FUNCION A NUESTRO METODO DE SORT
# GENERO UNA FUNCION -->ESTO NO ES SIEMPRE NECESARIO.


def order(element):
    return element[1]


users.sort(key=order)
# SI LA QUISIERA ORDENADA AL REVES
# users.sort(key=order, reverse=True)
# UNA MANERA MAS BONITA DE ESCRIBIR LO ANTERIOR SERIA USANDO LAMBDA:
# users.sort(key=lambda parametros:[valor de retorno], reverse=True)
# PERO, NO SIEMPRE ES BUENO USAR 'FUNCIONES ANONIMAS' O LAMBDA, ES UNA BUENA PRACTICA SI SOLO LA VOY A USAR UNA VEZ Y YA
# accedo al segundo elemento del listado.
users.sort(key=lambda el: el[1])
print(users)
