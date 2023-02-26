# PARA ESCRIBIR LA FUNCION USO LA PALABRA RESERVADA "DEF"
# LUEGO DE ESTO ESCRIBO EL NOMBRE DE LA FUNCION SEGUIDO DE ():
# Y ABAJO -IDENTADO- LO QUE VA A TENER MI FUNCION.
# Parametro es el nombre de la variable dentro de la funcion
# Si quiero mas de un parametro utilizo ',' para separar.
# En el caso de que no se pase un segundo argumento puedo agregar ="lo que se deberia agregar"
def hola(name, lastname="feliz"):
    print("Hola Mundo!")
    print(f"Welcome {name} {lastname}")


# Pep8 me agrega dos espacios despues de la funcion.
# con esto llamo a la funcion, de lo contrario quedaria guardado pero no mostraria nada.
hola("Sofia", "Michel")  # argumento es el valor que le estamos pasando
hola("Gala")

# ARGUMENTOS NOMBRADOS
hola(lastname="Michel", name="Sofia")
