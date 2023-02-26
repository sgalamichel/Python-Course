# FOR: GENERALMENTE LO USAMOS PARA ITERAR UNA LISTA DE ELEMENTOS
# TAMBIEN PARA PODER BUSCAR ELEMENTOS
# REALIZAR OPERACIONES MATEMATICAS, ETC.

# for number in range(5):  # nos devuelve una secuencia de 0 a 4.
#     # print(number)
#     print(number, number * 'Hola Mundo ')

# search = 3
# for number in range(5):
#     print(number)  # para ver cuantas veces se esta ejecutando el codigo
#     if number == search:
#         print("Found it! ", search)
#         break  # va a detener l ejecucion del codigo


search = 10
for number in range(5):
    print(number)  # para ver cuantas veces se esta ejecutando el codigo
    if number == search:
        print("Found it! ", search)
        break  # va a detener l ejecucion del codigo
    else:
        print("I didn't found it :( ")

for char in "Ultimate python":
    print(char)
