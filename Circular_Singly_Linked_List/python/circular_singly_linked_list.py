from node import Node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f"SinglyLinkedList({self.head})"

    def __eq__(self, other):
        if not isinstance(other, CircularSinglyLinkedList):
            return NotImplemented
        return self.to_array() == other.to_array()
    
    def __len__(self):
        return self.length

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def insert_at(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return self

    def find(self, value):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index) -> int | None:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range (index):
            current = current.next
        return current.value

    def remove(self, value) -> bool:
        if self.head is None:
            return False

        if self.head.next == self.head:
            if self.head.value == value:
                self.head = None
                self.length -= 1
                return True
            return False

        if self.head.value == value:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.length -= 1
            return True

        current = self.head
        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            if self.head.next == self.head:
                self.head = None
                self.length -= 1
                return self
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
                self.length -= 1
                return self

        current = self.head
        for _ in range (index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1
        return self

    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return self.head

        prev = self.head
        current = self.head.next

        while current != self.head:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head.next = prev
        self.head = prev
        return self

    def size(self) -> int:
            return self.length
        
    def is_empty(self) -> bool:
        return self.length == 0

    def to_array(self) -> list:
        array = []
        current = self.head
        if current is None:
            return array
        while True:
            array.append(current.value)
            current = current.next
            if current == self.head:
                break
        return array


    def print(self):
        current = self.head
        if current is None:
            print("None")
            return

        while True:
            print(current.value, end=" -> ")
            current = current.next

            if current == self.head:
                break
        print("(back to head)")


    def clear(self):
        self.head = None
        self.length = 0
        return self

    

    

    

    



