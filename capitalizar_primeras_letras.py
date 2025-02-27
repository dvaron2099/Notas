def capitalizar_primeras_letras(frase):
    """
    Función que recibe una cadena de texto y devuelve la misma frase con cada palabra capitalizada.
    Es decir, la primera letra en mayúscula y el resto en minúscula.
    """
    palabras = frase.split(' ')  # Dividimos la frase en una lista de palabras

    for i in range(len(palabras)):  # Iteramos sobre cada palabra en la lista
        palabra = palabras[i]  # Obtenemos la palabra actual
        palabras[i] = palabra.capitalize()  # Capitalizamos la primera letra y el resto en minúscula

    return ' '.join(palabras)  # Unimos la lista en una sola cadena separada por espacios

# Frase de ejemplo
frase = "esto es una frase de ejemplo"
frase_capitalizada = capitalizar_primeras_letras(frase)  # Llamamos a la función

# Mostramos el resultado
print(frase_capitalizada)  # Esto imprimirá "Esto Es Una Frase De Ejemplo"
