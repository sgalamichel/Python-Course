print("Welcome ")
print("To exit write exit ")
print("The operations are addition, subtraction, multiplication and division ")

resultado = ""
while True:  # loop infinito
    if not resultado:
        resultado = input("Input number: ")
        if resultado.lower() == "exit":
            break
        # transformo a numero entero sino ingreso el string de exit
        resultado = int(resultado)
    op = input("Input operation: ")
    if op.lower() == "exit":
        break
    n2 = input("Enter next number: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)

    if op.lower() == "addition":
        resultado += n2
    elif op.lower() == "subtraction":
        resultado -= n2
    elif op.lower() == "multiplication":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Invalid operation")
        break
    print(f"The result is {resultado}")  # string formateado, f.
