animal = "  peRRo feliz  "
# upper--->metodo= funcion que se encuentra dentro de un objeto
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())  # se puede encadenar metodos
print(animal.title())
# quita los espacios en blanco , puedo usar rstrip p lstrip o simplemente strip
print(animal.strip())
print(animal.find("RR"))
# nos va a devolver -1, lo que significa que no lo encontro, si fuera positivo en cambio si lo encontro
print(animal.find("rR"))  # no devuelve el indice
# tiene que recibir 2 argumentos, el primero es el que estamos buscando y el segundo por lo que tiene que reemplazar
print(animal.replace("RR", "l"))
print("eRR" in animal)  # nos devuelve true, un boolean
# busca si la cadena de caracteres no se encuentra dentro del string, otro boolean.
print("eRR" not in animal)
