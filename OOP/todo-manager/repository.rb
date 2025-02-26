class Repository
  def initialize
    @tasks = []     # -> Array de instancias de la clase Task
  end

  def add(task)
    @tasks << task   # -> # pusheando una instancia de la clase Task
  end
end
