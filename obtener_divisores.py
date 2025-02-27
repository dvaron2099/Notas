def obtener_divisores(numero):
    """
    Función que recibe un número y devuelve una lista con todos sus divisores.
    """
    divisores = []  # Lista vacía para almacenar los divisores

    for i in range(1, numero + 1):  # Iteramos desde 1 hasta el número
        if numero % i == 0:  # Si 'i' es divisor de 'numero'
            divisores.append(i)  # Lo agregamos a la lista

    return divisores  # Retornamos la lista de divisores

# Número del que queremos obtener los divisores
numero = 12  # Puedes cambiar este número para probar otros casos
divisores = obtener_divisores(numero)  # Llamamos a la función

# Mostramos el resultado
print(f"Los divisores de {numero} son: {', '.join(map(str, divisores))}")
