list1 = [1, 2, 3, 4]
# print(1, 2, 3, 4)
# print(*list1)

# PODEMOS COMBINAR LISTAS

list2 = [5, 6]

combinada = ["Hello", *list1, "world", *list2]
print(combinada)

# PODEMOS USAR ESTO TAMBIEN CON LOS DICCIONARIOS

point1 = {"x": 25, "y": "hi"}
point2 = {"y": 15}

# GENERO UN NUEVO PUNTO Y UTILIZO EL OPERADOR DE DESEMPAQUETAMEINTO **
# ME VA A DEVOLVER UN NUEVO DICCIONARIO CON LAS PROPIEDADES DEL PUNTO 1 Y 2 MAS LO QUE AGREGUE
newPoint = {**point1, "lala": "hello world", **point2, "z": "world"}
print(newPoint)
