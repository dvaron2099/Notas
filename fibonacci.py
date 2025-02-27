def fibonacci(n):
    """
    Función que genera la serie de Fibonacci hasta el término número 'n'.
    La serie de Fibonacci comienza con 0 y 1, y cada término siguiente
    es la suma de los dos anteriores.
    """
    fib_sequence = [0, 1]  # Inicializamos la serie con los dos primeros términos

    for i in range(2, n):  # Empezamos desde el índice 2 hasta n-1
        siguiente = fib_sequence[-1] + fib_sequence[-2]  # Suma de los dos últimos valores
        fib_sequence.append(siguiente)  # Agregamos el nuevo valor a la lista

    return fib_sequence[:n]  # Devolvemos solo los primeros 'n' términos

# Llamamos a la función y mostramos los primeros 10 términos
print(fibonacci(10))
