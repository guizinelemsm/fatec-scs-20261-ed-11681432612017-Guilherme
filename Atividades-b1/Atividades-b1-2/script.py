class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def appendafter(self,position,value):
        new_node = Node(value)
        if not self.head:
            print("list not found")
            return
        current = self.head
        while current:
            if current.value == position:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next





    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


lista = LinkedList()

lista.append(20)
lista.append(10)
lista.append(80)
lista.append(45)
lista.append(30)
lista.prepend(1000)
lista.prepend(4)
lista.appendafter(80,999)
lista.appendafter(30, 29)
lista.print_list()


