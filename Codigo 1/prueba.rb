def num_duplicates(name, price, weight)
  # Creamos un conjunto para almacenar productos únicos
  unique_products = Set.new
  # Contador para productos duplicados
  duplicate_count = 0

  # Iteramos sobre los productos
  name.each_with_index do |n, i|
    # Creamos una tupla con los atributos del producto
    product = [n, price[i], weight[i]]

    # Si el producto ya está en el conjunto, es un duplicado
    if unique_products.include?(product)
      duplicate_count += 1
    else
      # Si no está, lo añadimos al conjunto
      unique_products.add(product)
    end
  end

  return duplicate_count
end

# Ejemplo de uso
if __FILE__ == $0
  name = ["apple", "banana", "apple", "orange", "banana"]
  price = [1, 2, 1, 3, 2]
  weight = [100, 150, 100, 200, 150]

  puts num_duplicates(name, price, weight)  # Salida esperada: 2
end
