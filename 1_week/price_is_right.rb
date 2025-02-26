sup =1==
inf =1

price = rand(inf..sup)

puts "Ingrese el precio a adivinar entre 1 y 100"
user_price = gets.chom

if price == user_price
  puts "Adivinaste!!"
  puts "Tu numero fue: #{user_price} y el de la compu fue: #{price}"
else
  puts "Intenta de nuevo"
  puts "Tu numero fue: #{user_price} y el de la compu fue: #{price}"
end
