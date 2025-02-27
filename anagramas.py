import re  # Importamos la librería 're' para manejar expresiones regulares

def son_anagramas(word1, word2):
    """
    Función que comprueba si dos palabras son anagramas.
    - Ignora mayúsculas y minúsculas.
    - No considera espacios, símbolos, ni caracteres especiales.
    """
    # Convertimos ambas palabras a minúsculas y eliminamos caracteres que no sean letras
    palabra1 = re.sub(r'[^a-zA-Z]', '', word1.lower())
    palabra2 = re.sub(r'[^a-zA-Z]', '', word2.lower())

    # Si tienen diferente longitud, no pueden ser anagramas
    if len(palabra1) != len(palabra2):
        return False

    # Ordenamos los caracteres y comparamos las listas resultantes
    return sorted(palabra1) == sorted(palabra2)

# Pruebas
print(son_anagramas('Riesgo', 'Sergio'))  # True
print(son_anagramas('Riesgddo', 'Sergio'))  # False
