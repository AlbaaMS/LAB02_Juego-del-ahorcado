from juego_ahorcado import normalizar, enmascarar, ha_ganado

def test_normalizar():
    assert normalizar("Árbol") == "arbol"
    assert normalizar("Canción") == "cancion"
    assert normalizar("Ñandú") == "ñandu"
    assert normalizar("Python") == "python"
    assert normalizar("") == ""

def test_enmascarar():
    assert enmascarar("python", "py") == "py____"
    assert enmascarar("ahorcado", "oa") == "a_o__a_o"
    assert enmascarar("prueba", "") == "______"
    assert enmascarar("prueba", "i") == "______"
    assert enmascarar("prueba", "prueba") == "prueba"

def test_ha_ganado():
    assert ha_ganado("python") == True
    assert ha_ganado("p____n") == False
    assert ha_ganado("______") == False


test_normalizar()
test_enmascarar()
test_ha_ganado()

print("✅ Todas las pruebas han pasado correctamente.")

from juego_ahorcado import mostrar_estado
def test_mostrar_estado():
    assert mostrar_estado("p_th_n", ["a", "e", "i", "p", "t"], 5) == "Estado: p _ t h _ n"; "Letras usadas: 5"; "Intentos restantes: 5"

print("✅ Todas las pruebas han pasado correctamente.")