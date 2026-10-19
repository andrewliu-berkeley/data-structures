from node import Node
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f"DoublyLinkedList({self.head})"

    def __eq__(self, other):
        if not isinstance(other, DoublyLinkedList):
            return NotImplemented
        return self.to_array() == other.to_array()
    
    def __len__(self):
        return self.length

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return self


    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
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
        for _ in range (index):
            current = current.next
        new_node.previous = current.previous
        new_node.next = current
        current.previous.next = new_node
        current.previous = new_node

        self.length += 1
        return self

    def find(self, value):
        current = self.head
        while current is not None:
            if (current.value == value):
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

    def remove(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            self.length -= 1
            return True
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next.next is None:
                    current.next = None
                    self.tail = current
                    self.length -= 1
                    return True
                current.next = current.next.next
                current.next.previous = current
                self.length -= 1
                return True
            current = current.next
        return False
        
    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            self.length -= 1
            return self
        current = self.head
        for _ in range(index):
            current = current.next
        if current.next is not None:
            current.previous.next = current.next
            current.next.previous = current.previous
        else:
            current.previous.next = None
            self.tail = current.previous
        self.length -= 1
        return self

    def reverse(self):
        current = self.head

        self.head, self.tail = self.tail, self.head

        while current is not None:
            # Store next node original
            next_node = current.next

            # Reverse to pointer next previous
            current.next = current.previous
            current.previous = next_node

            # Transfer to next node origin
            current = next_node

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
            print(current.value, end="")

            if current.next is not None:
                print(" <-> ", end="")

            current = current.next

        print(" -> None")
        