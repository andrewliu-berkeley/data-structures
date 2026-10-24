
class Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            raise IndexError("Queue is full")

        self.rear += 1
        self.items[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")

        item = self.items[self.front]
        self.front += 1
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")

        item = self.items[self.front]
        return item

    def display(self):
        for i in range(self.front, self.front + self.size):
            print(self.items[i], end=" ")
        print()
            
    
    