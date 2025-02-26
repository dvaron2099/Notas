# Definimos una clase para el Nodo de la lista
class Node:
    def __init__(self, data):
        self.data = data  # Contiene el valor del nodo
        self.next = None  # Puntero al siguiente nodo, inicialmente es None

# Definimos la clase LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente la lista está vacía

    # Método para insertar un nuevo nodo al final de la lista
    def append(self, data):
        new_node = Node(data)  # Creamos un nuevo nodo
        if not self.head:
            self.head = new_node  # Si la lista está vacía, el nuevo nodo es la cabeza
            return
        last = self.head
        while last.next:  # Recorremos hasta el último nodo
            last = last.next
        last.next = new_node  # Asignamos el nuevo nodo al final de la lista

    # Método para imprimir los elementos de la lista
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Método para eliminar un nodo específico
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:  # Si el nodo a eliminar es el primero
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:  # Buscamos el nodo a eliminar
            prev = current
            current = current.next
        if current is None:  # Si el nodo no está presente
            return
        prev.next = current.next  # Eliminamos el nodo
        current = None

# Creamos una lista enlazada y probamos algunos métodos
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Lista original:")
llist.print_list()

llist.delete_node(3)  # Eliminamos el nodo con valor 3
print("\nLista después de eliminar el nodo con valor 3:")
llist.print_list()
