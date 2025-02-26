function numDuplicates(name, price, weight) {
  // Creamos un conjunto para almacenar productos únicos
  let uniqueProducts = new Set();
  // Contador para productos duplicados
  let duplicateCount = 0;

  // Iteramos sobre los productos
  for (let i = 0; i < name.length; i++) {
    // Creamos una tupla con los atributos del producto
    let product = [name[i], price[i], weight[i]];

    // Convertimos la tupla a una cadena para usarla en el Set
    let productString = JSON.stringify(product);

    // Si el producto ya está en el conjunto, es un duplicado
    if (uniqueProducts.has(productString)) {
      duplicateCount++;
    } else {
      // Si no está, lo añadimos al conjunto
      uniqueProducts.add(productString);
    }
  }

  return duplicateCount;
}

// Ejemplo de uso
let name = ["apple", "banana", "apple", "orange", "banana"];
let price = [1, 2, 1, 3, 2];
let weight = [100, 150, 100, 200, 150];

console.log(numDuplicates(name, price, weight));  // Salida esperada: 2
