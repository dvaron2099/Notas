def palindromo(palabra)
  separar = palabra.split('')
  reversar = separar.reverse
  unir = reversar.join('')
  if unir == palabra
    return true
  else
    return false
  end

end

puts palindromo('otto')
puts palindromo('victor')
