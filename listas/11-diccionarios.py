# LOS DICCIONARIOS SON UNA CONEXION DE DATOS QUE SE ENCUENTRAN AGRUPADOS POR UNA LLAVE Y UN VALOR
# es como las bases de datos nos devuelven los datos

point = {"x": 25, "y": 50}
print(point)
print(point["x"])
print(point["y"])

# PODEMOS AGREGAR MAS LLAVES A LOS DICCIONARIOS BAJO DEMANDA

point["z"] = 45

# QUIERO ACCEDER A ALGUN VALOR QUE SE ENCUENTRA DENTRO DEL DICCIONARIO CUYA LLAVE NO EXISTE
# PRIMERO PREGUNTO SI EL VALOR SE ENCUENTRA DENTRO DEL PUNTO

if "lala" in point:
    print("I found lala", point["lala"])

# METODO GET PARA ACCEDER A UN VALOR DENTRO DEL DICCIONARIO
print(point.get("x"))
# QUE PASARIA SI POR ALGUNA RAZON EL VALOR NO EXISTIERA?
print(point.get("lala"))  # --> nos devuelve None
# si no existe el valor puedo agregar un valor por defecto
print(point.get("lala", 97))
# SI QUIERO ELIMINAR ALGUNAS DE LAS LLAVES INCLUYENDO SU VALOR :
del point["x"]
# SI QUIERO ELIMINAR UNA LLAVE INCLUIDA EN EL DICCIONARIO
del (point["y"])

print(point)

point["x"] = 25

# SI QUIERO ITERAR TODAS LAS LLAVES CON SU VALOR DENTRO DE PYTHON PUEDO HACERLO CON UN 'FOR'
for valor in point:
    print(valor, point[valor])

for valor in point.items():
    print(valor)  # me devuelve tuplas

# puedo hacer un desempaquetado de las tuplas
for llave, valor in point.items():
    print(llave, valor)

users = [
    {"id": 1, "name": "Franco"},  # identificador unico - id
    {"id": 2, "name": "Jamie"},
    {"id": 3, "name": "Nicolas"},
    {"id": 4, "name": "Ruben"},
    {"id": 5, "name": "Patrick"},
]

# QUIERO ACCEDER SOLO A LOS NOMBRES
# ITERO LOS USUARIOS

for user in users:
    print(user["name"])
