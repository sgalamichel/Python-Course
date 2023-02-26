# CREO FUNCION PARA QUITAR ESPACIO

def no_space(text):
    # VOY A IR ALMACENANDO EL TEXTO DE LA NUEVA FUNCION,
    # COMIENZA CON UN STRING VACIO,TOMO EL STRING QUE RECIBO COMO PARAMETRO,
    # LO ITERO Y CONCATENO C/U DE LOS CARACTERES CON NUEVO TEXTO SIEMPRE Y CUANDO ESTE NO SEA UN STRING VACIO.
    new_text = ""
    for char in text:
        if char != " ":  # CHAR ES DISTINTO A UN ESPACIO?
            new_text += char  # CONCATENO UN STRING CON EL OTRO A MENOS QUE SEA UN ESPACIO EN BLANCO
    return new_text

# CREO FUNCION PARA DAR VUELTA EL TEXTO


def reverse(text):
    reverse_text = ""  # CREO VARIABLE Y LA IGUALO A UN STRING VACIO
    for char in text:  # ITERO EL TEXTO
        # CONCATENO LOS CARACTERES A LA IZQ(VA A DAR VUELTA EL STRING)
        reverse_text = char + reverse_text
    return reverse_text

# FUNCION PARA SABER SI EL TEXTO ES UN PALINDROMO


def is_palindrome(text):
    text = no_space(text)
    reverse_text = reverse(text)
    # print(reverse_text)
    # RETORNO TEXTO Y LO COMPARO CON EL TEXTO AL REVES, ME DEBE DEVOLVER UN BOOLEAN
    # APLICO METODO LOWER A C/U DE LAS VARIABLES POR SI ESCRIBO CON MAYUSCULAS O MINUSCULA
    return text.lower() == reverse_text.lower()


print(is_palindrome("Amo la paloma"))  # RETORNARA TRUE
print(is_palindrome("HOLA MUNDO"))  # RETORNARA FALSE
# print("Abba", is_palindrome("Abba"))
# print("Level", is_palindrome("Level"))
# print("Amo la paloma", is_palindrome("Amo la paloma"))
# print("Hola mundo", is_palindrome("hola mundo"))

# ELIMINAR LOS ESPACIOS EN BLANCO DE UN STRING
# TOMAR UN TEXTO --> REVERSE
# CONSTRUYO REVERSE CON FOR E ITERO C/U DE LOS CARACTERES Y
# DEPENDIENDO DEL CARACTER QUE RECIBO LE APLICO UNA FUNCION O NO
