#linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        while current_node:
            print(f"{current_node.data}")
            current_node = current_node.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_after_value(self, data_after, data_to_insert):
        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                new_node = Node(data_to_insert)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def remove_by_value(self, value_to_remove):
        if self.head == None:
            print("Lista jest pusta")
            return
        
        if self.head.data == value_to_remove:
            self.head = self.head.next
            return
         
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value_to_remove:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        print(f"Nie znaleziono wartości {value_to_remove} w liście.")
        print("\n")


ll = LinkedList()
fruits = ["banana", "mango", "grapes", "orange"]
for fruit in fruits:
    ll.append(fruit)
ll.print()
print("\n")
ll.insert_after_value("mango","apple")
ll.print()
print("\n")
ll.remove_by_value("orange")
ll.print()
print("\n")
ll.remove_by_value("figs")
ll.print()
print("\n")
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
print("\n")

#double linked list

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data  
        self.next = next  
        self.prev = prev  

class DoublyLinkedList:
    def __init__(self):
        self.head = None  
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
            return
        last_node = self.head
        while last_node.next: 
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def print_backward(self):
        if self.head is None:
            print("The list is empty")
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        print("List in backward direction:")
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.prev
        print()

dll = DoublyLinkedList()

dll.append("banana")
dll.append("mango")
dll.append("grapes")
dll.append("orange")

dll.print_backward()


