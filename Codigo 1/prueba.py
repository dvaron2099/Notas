def numDuplicates(name, price, weight):
    # Creamos un conjunto para almacenar productos únicos
    unique_products = set()
    # Contador para productos duplicados
    duplicate_count = 0

    # Iteramos sobre los productos
    for i in range(len(name)):
        # Creamos una tupla con los atributos del producto
        product = (name[i], price[i], weight[i])

        # Si el producto ya está en el conjunto, es un duplicado
        if product in unique_products:
            duplicate_count += 1
        else:
            # Si no está, lo añadimos al conjunto
            unique_products.add(product)

    return duplicate_count

if __name__ == '__main__':
    # Ejemplo de uso
    name = ["apple", "banana", "apple", "orange", "banana"]
    price = [1, 2, 1, 3, 2]
    weight = [100, 150, 100, 200, 150]

    print(numDuplicates(name, price, weight))  # Salida esperada: 2
