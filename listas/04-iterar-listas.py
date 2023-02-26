pets = ["Arya", "Emma", "Tommy", "Floki"]

for pet in pets:
    print(pet)

# QUIERO ACCEDER AL INDICE DEL ELEMENTO QUE ESTOY ITERANDO
# ME VA A DEVOLVER UN LISTADO DE TUPLAS-->ENUMERATE

for pet in enumerate(pets):
    print(pet)

# DE ESTA MANERA PUEDO OBTENER LOS INDICES DE UNA LISTA
fist, second = [1, 2]
for index, pet in enumerate(pets):
    print(index, pet)
