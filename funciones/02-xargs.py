# XARG - QUIERO PASAR MULTIPLES ARGUMENTOS A LA FUNCION

def adittion(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


adittion(2, 5, 7)
adittion(2, 5)
adittion(2, 5, 7, 54)
