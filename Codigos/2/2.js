/*
  Dada una cadena de texto, comprobar si es un palindromo o no.
  Los palidromos son palabras que se leen igual aun estando invertidas.
  Por ejemplo: ana, bob, otto, allivessevilla

  Ejemplos:
  - Ejecuta esta funcion:
  palindromo("otto") // devuelve:true
  palindromo("victor") // devuelve:false
 */


function palindromo(palabra) {
  let separar = palabra.split('')
  let vuelta = separar.reverse()
  let union = vuelta.join('')
  if (palabra == union) {
    return true
  } else {
    return false
  }
}

console.log(palindromo('otto'))
console.log(palindromo('Victor'))
