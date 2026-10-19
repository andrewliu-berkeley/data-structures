from node import Node
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f"SinglyLinkedList({self.head})"

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList):
            return NotImplemented
        return self.to_array() == other.to_array()
    
    def __len__(self):
        return self.length

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert_at(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return self

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def get(self, index) -> int | None:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, value) -> bool:
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if (current.next.value == value):
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False
    
    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return self
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1
        return self
    
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        return self
    
    def size(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def to_array(self) -> list:
        array = []
        current = self.head
        while current is not None:
            array.append(current.value)
            current = current.next
        return array

    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def clear(self):
        self.head = None
        self.length = 0
        return self