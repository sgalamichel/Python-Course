# forma de obtener datos del usuario -->input

n1 = input("Enter the first number")
n2 = input("Enter the second number")

n1 = int(n1)
n2 = int(n2)

addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

# devo colocar la f para que el mensaje sea correctamente interpretado.
message = f"""  
For the numbers {n1} and {n2},
the result of the addition is {addition}.
the result of the subtraction is {subtraction}.
the result of the multiplication is {multiplication}.
the result of the division is {division}.
"""
print(message)
