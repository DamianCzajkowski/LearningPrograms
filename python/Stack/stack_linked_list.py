class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:

    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return '\n'.join(values)

    def is_empty(self):
        return not bool(self.linked_list.head)

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def peek(self):
        if self.is_empty():
            return "List is empty!"
        return self.linked_list.head.value

    def pop(self):
        if self.is_empty():
            return "List is empty!"

        if self.linked_list.head.next is None:
            value = self.linked_list.head.value
            self.linked_list.head = None
            return value
        value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return value

    def delete(self):
        self.head = None


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
print("-------------")
print(stack)
