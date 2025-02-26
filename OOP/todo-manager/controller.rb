require_relative 'task'

class Controller

  def initialize(view, repository)
    @repository = repository
    @view = view
  end

  def add_task
    # 1. Preguntarle al usuario que tarea quiere agregar[view]
    title = @view.ask_user_for_title
    # 2. Crear una instancia de la tarea
    task = Task.new(title)
    # 3. La guardamos en el repository
    @repository.add(task)
  end
end
