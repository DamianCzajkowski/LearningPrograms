class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def insert(self, value, location=-1):
        if self.head is None:
            self.create(value)
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1 and temp_node != self.tail:
                    temp_node = temp_node.next
                    index += 1
                if temp_node == self.tail:
                    new_node.next = self.tail.next
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    next_node = temp_node.next
                    temp_node.next = new_node
                    new_node.next = next_node

    def traverse(self):
        if self.head is None:
            print('The circular linked list doesnt have any value')
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    def search(self, value):
        if self.head is None:
            return 'The circular linked list doesnt have any value'
        index = 0
        node = self.head
        while node:
            if node.value == value:
                return index
            node = node.next
            index += 1
            if node == self.tail.next:
                break
        return 'The value does not exists in this list'

    def remove(self, location):
        if self.head is None:
            return 'The circular linked list doesnt have any value'
        if location == 0:
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        if location == -1:
            if self.tail == self.head:
                self.tail = None
                self.head = None
            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            temp_node = self.head
            index = 0
            while index < location - 1 and temp_node != self.tail:
                temp_node = temp_node.next
                index += 1
            if temp_node == self.tail:
                temp_node.next = self.head
                self.tail = temp_node
            else:
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete(self):
        if self.head is None:
            print('The circular linked list doesnt have any value')
        else:
            self.head = None
            self.tail = None


if __name__ == "__main__":

    circular_linked_list = CircularSinglyLinkedList()
    circular_linked_list.insert(1)
    circular_linked_list.insert(2)
    circular_linked_list.insert(3)
    circular_linked_list.insert(4)
    circular_linked_list.insert(5)
    circular_linked_list.insert(6)
    circular_linked_list.insert(0, 0)
    circular_linked_list.insert(0, 3)
    circular_linked_list.insert(0, -1)
    circular_linked_list.insert(9, 9)
    circular_linked_list.insert(123321, 1231231231)
    circular_linked_list.traverse()

    print(circular_linked_list.search(3))

    print([node.value for node in circular_linked_list])

    circular_linked_list.remove(0)
    circular_linked_list.remove(1)
    circular_linked_list.remove(-1)
    circular_linked_list.remove(6)

    print([node.value for node in circular_linked_list])

    circular_linked_list.delete()
    circular_linked_list.delete()

    print([node.value for node in circular_linked_list])
