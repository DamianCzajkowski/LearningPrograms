class Stack:

    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    def is_empty(self):
        return not bool(self.list)

    def is_full(self):
        return len(self.list) == self.max_size

    def push(self, value):
        if self.is_full():
            return 'Stack is full!!'
        self.list.append(value)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty!'
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return 'Stack is empty!'
        return self.list[-1]

    def delete(self):
        self.list = []


stack = Stack()
print(stack.is_empty())
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack)
print(stack.is_empty())
print(stack.peek())
print(stack.pop())
