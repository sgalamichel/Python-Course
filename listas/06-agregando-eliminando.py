pets = [
    "Arya",
    "Emma",
    "Tommy",
    "Floki",
    "Tommy",
    "Sam",
    "Harry"
]

# QUIERO HACER ESPACIO EN EL INDICE 1 Y AGREGARLE UN NUEVO VALOR--> METODO 'INSERT'
# .insert(indice donde quiero agregar el elemento, "valor que quiero ingresar dentro d ese indice")
pets.insert(1, "Chispa")
# SI QUISIERA AGREGAR EL ELEMENTO AL FINAL DE LA LISTA --> .append
pets.append("Nicole")


# ELIMINAR ELEMENTOS QUE SE ENCUENTRAN DENTRO DE UN LISTADO
# .remove("elemento que quiero eliminar")
# SI EXISTE MAS DE UN ELEMNTO CON EL MISMO NOMBRE DEBERIA HACER UN CONTEO PRIMERO

pets.remove("Sam")

# SI QUISIERA ELIMINAR EL ULTIMO ELEMENTO DE UN ARREGLO -->'listado'.pop
pets.pop()

# OTRO METODO PARA ELIMINAR ELEMENTOS DENTRO DE UN ARREGLO ES 'del' (palabra reservada)
# seguido del listado al cual le queremos eliminar el elemento [y el indice]

del pets[3]

# SI QUIESIERA LIMPIAR COMPLETAMENTE LA LISTA --> '.clear()

pets.clear()

print(pets)
