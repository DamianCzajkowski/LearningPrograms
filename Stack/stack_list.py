class Stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    def is_empty(self):
        return not bool(self.list)

    def push(self, value):
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
