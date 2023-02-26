# and, or, not (la operacion evalua con 'and' si ambas son True, si alguno es False deberia ir con 'or'. Not niega el resultado de una operacion )

gas = True
encendido = True
age = 18

# if gas and encendido:
#     print("Go ahead") si ambos son True


# if gas or encendido:
#     print("Go ahead") basta con que uno sea True

# if not gas and encendido:
#     print("Go ahead")   not cambia el valor, si es false a true y viceversa

if not gas and (encendido or age > 17):
    print("Go ahead")

# operador cortocircuito--> and: si la expresion de la derecha retorna falso la de la dereccha no se va a ejecutar
# or: basta con que la expresion de la izq sea True para que no se evalue la de la derecha, pero si sucede lo contrario si lo hara.
