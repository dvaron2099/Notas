require "date"

def day_until_xmas(someday)
  xmas = Date.new(2023,12,25)
  day_until = (xmas - someday).to_i
  if day_until.negative?
    "Estoy pidiendo el año actual"
  else
    day_until
  end
end


puts day_until_xmas(Date.new(2023,12,24))
