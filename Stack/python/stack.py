class Stack:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        if self.top == self.capacity - 1:
            print("Stack overflow")
            return self

        self.top += 1
        self.items[self.top] = value
        return self

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return None

        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            print("Stack underflow")
            return None
        value = self.items[self.top]
        return value

    def peek_from_top(self, index):
        if index >= self.top:
            print("Stack item not exist")
            return None
        temp = self.top
        for _ in range (index):
            temp -= 1
        return self.items[temp]

    def display(self):
        print(self.items[:self.top + 1])
