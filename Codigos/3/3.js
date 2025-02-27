/*
  Dada una palabra, buscarla en una frase y devolver cuantas veces aparece en ella.
  la frase y la palabra deben ser parametros de una funcion.

  Ejemplos:
  coincidencias("hola soy una palabra en una frase, PALABRA.", "palabra") // Devuelve = 2
  coincidencias("soy la frase", "palabra") // Devuelve = 0
*/

function coincidencias(frase, palabra) {
  let textClean = frase.toLocaleLowerCase().replace(/[^\w\s]/gi, '')
  //let texSparate = textClean.split('')
  let count = 0

  if (texClean.includes(palabra)) {
    count += 1
  }
  else
  if (texClean.includes(palabra)) {
    count += 1
  } else {
    count = 0
  }
}
