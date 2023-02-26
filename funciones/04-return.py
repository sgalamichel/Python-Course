# RETURN --> nos va a permitir tomar la variable de resultdo en este caso y devolverla cada vez que llamemos a la funcion de suma

def adittion(a, b):
    result = a + b
    return result


c = adittion(1, 2)
d = adittion(c, 2)

print(d)
