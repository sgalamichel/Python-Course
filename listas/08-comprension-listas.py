users = [
    ["Ana", 4],
    ["Jonh", 5],
    ["Kevin", 22],
    ["Philliph", 8],
]

# DE ESTO LISTADO DE USUARIOS QUE TENEMOS QUEREMOS OBTENER SOLO EL NOMBRE, EL IDENTIFICADOR NO NOS INTERESA.
# TOMAMOS LA LISTA DE USUARIO->TRASFORMACION=LISTA DE NOMBRES

# con for iteramos, creamos una variable y con el metodo de append vamos agregando c/u de los nombres
# names = []
# for user in users:
#     names.append(user[0])
# print(names)

# PERO EXISTE OTRA MEJOR FORMA DE REDACTAR ESTO EN SOLO UNA LINEA
# names = [expresion for item in items] --.podria usar map
# 0 porque es el primer elemento el que quiero, el nombre.
# names = [user[0] for user in users]

# EN LUGAR DE TRANFORMAR EL LISTADO QUIERO FILTRARLO
# names = [expresion for item in items]
# pero en este caso quiero que cumplan la condicion que los indices [1] sean mayores a 5
# names = [user for user in users if user[1] > 5]

# AHORA QUIERO FILTRAR Y TRANFORMAR - podria usar filter
# names = [user[0] for user in users if user[1] > 5]

# OBTENGO USUARIOS UTILIZANDO MAP
names = list(map(lambda user: user[0], users))
print(names)

# OBTENGO USUARIOS CON INDICE MAYOR A 5 UTILIZANDO FILTER

menosusers = list(filter(lambda user: user[1] > 5, users))
print(menosusers)
