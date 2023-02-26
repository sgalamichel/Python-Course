# # QUIERO QUE EL NUMERO SE MULTIPLIQUE X 2 MIENTRAS SEA MENOR QUE 100
# number = 1
# while number < 100:  # primero evalua
#     print(number)
#     number *= 2


comando = ""

# .lower() me va a salvar cuando el usuario escriba salir con alguna mayuscula por ejemplo.
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)


# LOOP INFINITO, CUANDO NO TENEMOS UNA CONDICION DE SALIDA Y POR ENDE EL LOOP SE ESTARIA EJECUTANDO SIEMPRE.
# CTRL + C PARA PARARLO


# .lower() me va a salvar cuando el usuario escriba salir con alguna mayuscula por ejemplo.
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":  # siempre agreamos una condicion de salida cuando tenemos un loop infinito
        break
