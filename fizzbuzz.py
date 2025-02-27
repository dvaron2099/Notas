def fizzbuzz(n):
    """
    Función que imprime los números del 1 al n, pero:
    - Si el número es múltiplo de 3, imprime "Fizz".
    - Si el número es múltiplo de 5, imprime "Buzz".
    - Si el número es múltiplo de ambos (3 y 5), imprime "FizzBuzz".
    - De lo contrario, imprime el número.
    """
    for i in range(1, n + 1):  # Itera desde 1 hasta n
        if i % 3 == 0 and i % 5 == 0:  # Si es múltiplo de 3 y 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Si es múltiplo de 3
            print("Fizz")
        elif i % 5 == 0:  # Si es múltiplo de 5
            print("Buzz")
        else:  # Si no es múltiplo de 3 ni de 5
            print(i)

# Llamamos a la función con un valor de prueba
fizzbuzz(20)
