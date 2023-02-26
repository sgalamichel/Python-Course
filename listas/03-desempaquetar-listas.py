numbers = [1, 2, 3]

# NO ES CORRECTO, QUEDA MAL
# first = numbers[0]
# second = numbers[1]
# thrid = numbers[2]

# LA MANERA CORRECTA DE OBTENER LOS ELEMENTOS DE LA LISTA
first, second, thrid = numbers
print(first, second, thrid)

# SI SOLO QUEREMOS OBTENER UNO EN CAMBIO (en este caso el primero)
first, *others = numbers
print(first)
# print(first, others)

# QUE SUCEDE CUANDO TENGO MAS ELEMENTOS?
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# QUIERO OBTENER EL PRIMER Y SEGUNDO ELEMENTO
first, second, *others = numbers2
print(first, second, others)
# QUIERO OBTENER EL PRIMER Y ULTIMO ELEMENTO
fisrt, *others, last = numbers2
print(fisrt, last, others)
# QUIERO OBTENER EL SEGUNDO Y PENULTIMO ELEMENTO
first, second, *others, secondLast, last = numbers2
print(second, secondLast, others)
