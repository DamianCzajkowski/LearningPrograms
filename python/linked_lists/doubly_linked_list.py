class Node:

    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        return "DoublyLinkedList is created!"

    def insert(self, value, position):
        if self.head is None:
            print("The node cannot be inserted. List is empty!")
        else:
            new_node = Node(value)
            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif position == -1:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = temp_node
                temp_node.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node)
                temp_node = temp_node.next

    def reverse_traverse(self):
        if self.tail is None:
            print("List is empty!")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node)
                temp_node = temp_node.prev

    def search(self, value):
        if self.head is None:
            return 'List is empty!'
        index = 0
        node = self.head
        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return 'The value does not exists in this list'

    def remove(self, position):
        if self.head is None:
            print("List is empty!")
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif position == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.prev
                    self.head.next = None
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node

    def delete(self):
        if self.head is None:
            print("There is not any node in list")
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
