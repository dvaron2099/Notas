def numero_mayor(num1, num2):
    """
    Función que recibe dos números y determina cuál es el mayor.
    Si ambos números son iguales, lo indica.
    """
    if num1 > num2:
        print(f"{num1} es el número mayor")  # Si num1 es mayor que num2
    elif num1 < num2:
        print(f"{num2} es el número mayor")  # Si num2 es mayor que num1
    else:
        print(f"{num1} y {num2} son el mismo número")  # Si son iguales

# Llamamos a la función con distintos valores
numero_mayor(3, 5)
numero_mayor(10, 5)
numero_mayor(5, 5)
