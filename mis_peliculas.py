def mis_peliculas(peliculas):
    """
    Función que recibe una lista de diccionarios con información sobre películas.
    Para cada película:
    - Si ha sido vista, muestra 'Me he visto [título] de [director]'.
    - Si no ha sido vista, muestra 'Me falta por ver [título] de [director]'.
    """
    for pelicula in peliculas:  # Iteramos sobre la lista de películas
        para_mostrar = f"{pelicula['titulo']} de {pelicula['director']}"  # Formateamos la salida

        if pelicula['vista']:  # Si 'vista' es True
            print(f"Me he visto {para_mostrar}")
        else:  # Si 'vista' es False
            print(f"Me falta por ver {para_mostrar}")

# Lista de películas con título, director y si han sido vistas
peliculas = [
    {"titulo": "El señor de los anillos", "director": "Peter Jackson", "vista": True},
    {"titulo": "La Liga de la Justicia", "director": "Zack Snyder", "vista": False},
    {"titulo": "Los Vengadores: Endgame", "director": "Joe Russo", "vista": True},
    {"titulo": "Batman vs Superman", "director": "Zack Snyder", "vista": False}
]

# Llamamos a la función para mostrar los resultados
mis_peliculas(peliculas)
