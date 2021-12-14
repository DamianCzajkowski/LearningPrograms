from typing import Any


class Node:

    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.next = None


class SingleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> Node:
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value: Any, location: int = -1) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1 and temp_node.next is not None:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head is None:
            print('The singly linked list doesnt have any value')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, value):
        if self.head is None:
            return 'The singly linked list doesnt have any value'
        index = 0
        node = self.head
        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return 'The value does not exists in this list'

    def remove(self, location=-1):
        if self.head is None:
            print('The singly linked list doesnt have any value')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1 and temp_node.next.next is not None:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
                if temp_node == self.tail:
                    self.tail.next = None

    def delete(self):
        if self.head is None:
            print('The singly linked list doesnt have any value')
        else:
            self.head = None
            self.tail = None


if __name__ == "__main__":
    singly_linked_list = SingleLinkedList()
    singly_linked_list.insert(1)
    singly_linked_list.insert(2)
    singly_linked_list.insert(3)
    singly_linked_list.insert(4)
    singly_linked_list.insert(5)
    singly_linked_list.insert(6)
    singly_linked_list.insert(0, 0)
    singly_linked_list.insert(0, 3)
    singly_linked_list.insert(0, -1)
    singly_linked_list.insert(9, 9)
    singly_linked_list.insert(123321, 1231231231)
    singly_linked_list.traverse()

    print(singly_linked_list.search(3))

    print([node.value for node in singly_linked_list])
    singly_linked_list.remove(0)
    singly_linked_list.remove(1)
    singly_linked_list.remove(-1)
    singly_linked_list.remove(8)
    print([node.value for node in singly_linked_list])
    singly_linked_list.delete()
    singly_linked_list.delete()
    print([node.value for node in singly_linked_list])
