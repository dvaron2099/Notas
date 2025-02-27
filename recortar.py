def recortar(frase, numero):
    """
    Función que recibe una cadena de texto y un número.
    Devuelve los primeros 'numero' caracteres de la frase,
    eliminando los espacios en blanco antes del recorte.
    """
    recorte = ''.join(frase.split()).[:numero]  # Eliminamos espacios y tomamos los primeros 'numero' caracteres
    return recorte

# Prueba de la función
print(recortar('Cursos Desarrollo Web', 6))  # Devuelve: 'Cursos'
