class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.top = None
        self.min_node = None

    def push(self, value):
        if self.min_node and value > self.min_node.value:
            self.min_node = Node(self.min_node.value, self.min_node)
        else:
            self.min_node = Node(value, self.min_node)
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return "List is empty!"

        self.min_node = self.min_node.next
        item = self.top.value
        self.top = self.top.next
        return item

    def min(self):
        if self.min_node:
            return self.min_node.value
        return None


stack = Stack()

stack.push(5)
stack.push(6)
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(1)
stack.push(4)
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
