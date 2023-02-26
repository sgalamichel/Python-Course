pets = ["Arya", "Emma", "Tommy", "Floki"]
# print(pets[0])
pets[0] = "pulga"
print(pets[0])
# print(pets[0:3])
# print(pets[2:])
# print(pets[-1])
# print(pets[::2])#pares, toma el primer elemento, el siguiente lo salta y asi sucesivamente

numbers = list(range(21))
# numbers = list(range(1, 21)) #TAMBIEN ME VA A DEVOLVER IMPARES
# VA A DEVOLVER TODOS LOS NUMEROS IMPARES, EMPIEZA EN 1 EL DOS LO SALTA, TOMA EL 3 ....
print(numbers[1::2])
print(numbers[::2])  # VA A DEVOLVER TODOS LOS NUMEROS PARES
