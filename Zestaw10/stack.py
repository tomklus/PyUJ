class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):                  # podgladamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pelny
        return False

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")

        self.items.append(item)

    def pop(self):      
        if self.is_empty():
            raise IndexError("Stack is empty")                # zwraca element

        return self.items.pop()         # zabieram od konca
