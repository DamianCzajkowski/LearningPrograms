class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        return not self.items

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty!'
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return 'Queue is empty!'
        return self.items[0]

    def delete(self):
        self.items = None
