# Cat.new(...) -> Ejecutando el metodo
# initialize
class Cat
  attr_reader :color, :name
  def initialize(color, name)
    @color = color
    @name = name
  end

  #behaviour
  def dye(new_color)
    @color = new_color
  end
  def self.specie
    return "Mammals"
  end
end


## Testing
#cat = Cat.new("black", "Kitty")
#
#puts "#{cat.name} is #{cat.color}"
#
#puts "--------------"
#cat.dye("White")
#puts "--------------"
#
#puts "#{cat.name} is #{cat.color}"

p Cat.specie
