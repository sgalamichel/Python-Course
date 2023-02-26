# UNA TUPLA ES LO MISMO QUE UNA LISTA, SOLO QUE NO ES MODIFICABLE.
# PERO SI PUEDO CREAR OTRAS TUPLAS/LISTAS EN BASE A TUPLAS YA EXISTENTES.
# VAMOS A QUERER UTILIZAR LAS TUPLAS CUANDO NO QUERAMOS DE MANERA ACCIDENTAL
# MODIFICAR LOS ELEMENTOS QUE SE ENCUENTRA DENTRO DE ALGUN LISTADO.

numbers = (1, 2, 3) + (4, 5, 6)
print(numbers)

# QUIERO TRANSFORMAR ESTE LISTADO EN UNA TUPLA
# point = [1, 2] --> utilizo 'tuple()' la cual recibe cualquier cosa que sea iterable.
point = tuple([1, 2])
print(point)

# ACCEDO A ELEMETO DE LA TUPLA - GENERO UNA NUEVA LISTA
menosNumers = numbers[:2]
print(menosNumers)

# DESEMPAQUETO TUPLA
fisrt, second, *others = numbers
print(fisrt, second, others)

# ITERO TUPLA
for n in numbers:
    print(n)

# SI POR ALGUNA RAZON DEBO MODIFICAR UNA TUPLA LO CORRECTO SERIA CREAR UN NUEVA VARIABLE

listNumbers = list(numbers)
listNumbers[0] = "Albert"
print(listNumbers)
