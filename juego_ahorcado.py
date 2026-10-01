
def normalizar (texto):
    texto = texto.lower() 
    texto = texto.strip() 
    for letras in texto:
        if letras in "áéíóúü":
            texto = texto.replace("á","a")
            texto = texto.replace("é", "e")
            texto = texto.replace("í", "i")
            texto = texto.replace("ó", "o")
            texto = texto.replace("ú" or "ü", "u")
    return texto

def enmascarar (palabra,letra):

    palabra_prueba = ""
    for c in palabra:
        if c not in letra:
            palabra_prueba = palabra_prueba + "_"
        else:
            palabra_prueba = palabra_prueba + c
    return palabra_prueba

def ha_ganado (enmascarar=True):
    if "_" not in enmascarar:
        True
    else:
        False
    return ha_ganado