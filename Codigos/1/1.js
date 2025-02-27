function tablaMultiplicar(numero) {
  let header = `# Tabla del ${numero} #`
  console.log(header)
  let num = numero
  for (let i = 1; i <= 10; i++){
    let multi = i * num
    console.log(`${i} x ${num} = ${multi}`)
  }
}

tablaMultiplicar(2)
