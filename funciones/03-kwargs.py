# SIEMPRE AGREGO ** ANTES DEL PARAMETRO CUANDO USO KWARGS

def get_product(**datos):
    # QUE PASARIA SI SOLO NECESITO 2 PARAMETROS ??
    # PARA ELLO UTILIZO DENTRO DE PRINT (datos["AQUI DENTRO EL NOMBRE DEL PARAMETRO AL CUALQUIERO ACCEDER"], datos["EL OTRO PARAMETRO QUE NECESITO"]
    print(datos["id"], datos["name"])

# LOS ARGUMENTOS VAN A DEMANDA, PUEDO PASAR VARIOS.
# SIEMPRE TENGO QUE PASAR EL NOMBRE DEL PARAMETRO.


get_product(id="23",
            name="iPhone",
            desc="This is an iPhone")
