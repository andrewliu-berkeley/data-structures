class Stack:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        if self.top == self.capacity - 1:
            raise IndexError("Stack overflow")

        self.top += 1
        self.items[self.top] = value
        return self

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack overflow")

        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        
        value = self.items[self.top]
        return value

    def peek_from_top(self, index):
        if index < 0 or index >= self.top:
            raise IndexError("Stack underflow/overflow")
        temp = self.top
        for _ in range (index):
            temp -= 1
        return self.items[temp]

    def display(self):
        print(self.items[:self.top + 1])
