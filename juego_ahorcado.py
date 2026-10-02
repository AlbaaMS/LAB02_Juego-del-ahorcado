'''
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

def ha_ganado(enmascarar):
    for i in enmascarar:
        if "_" in i:
            return False
    return True

def mostrar_estado(enmascarada,letras, intentos):
    """Muestra en la pantalla el estado actual del juego.

    Parámetros:
    enmascarada (str): La palabra con las letras adivinadas y guiones bajos.
    letras (list o str): Conjunto de letras que el jugador ya ha intentado.
    intentos (int): Número de intentos que le quedan al jugador.
    """
    enmascarada = " ".join(enmascarada)
    if not  letras:
        letras = "ninguna" 
    print(f"Estado: {enmascarada}")
    print(f"Letras usadas: {letras}")
    print(f"Intentos restantes: {intentos}")
'''
def pedir_letra(letras_usadas):
    """Solicita una letra al jugador y valida que sea correcta.

    Pide una letra por teclado y verifica que sea un único carácter
    alfabético y que no haya sido utilizada previamente. Repite la
    solicitud hasta que la entrada sea válida.

    Parameters:
        letras_usadas (list of str): Lista con las letras (en minúsculas)
            que el jugador ya ha solicitado anteriormente.

    Returns:
        str: La letra válida introducida por el jugador, en minúsculas.
    """
    while True:
        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Debes introducir una única letra del abecedario.")
        elif letra in letras_usadas:
            print("Esa letra ya la has usado anteriormente.")
        else:
            return letra

# Ejemplo de uso pasándole una lista inicial de letras usadas:
usadas = ["a", "e", "i"]
letra_elegida = pedir_letra(usadas)
print(f"Letra válida elegida: {letra_elegida}")
