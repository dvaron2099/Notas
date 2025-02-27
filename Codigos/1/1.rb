def tabla_multiplicar(numero)
  header = "# Tabla del #{numero} #"
  puts header
  (1..10).each do |i|
    multi = i * numero
    puts "#{i} x #{numero} = #{multi}"
  end
end

tabla_multiplicar(2)
