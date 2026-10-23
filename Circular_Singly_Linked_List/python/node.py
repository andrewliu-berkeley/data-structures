class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return self.value == other.value