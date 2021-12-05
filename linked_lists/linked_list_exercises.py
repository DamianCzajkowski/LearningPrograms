from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self

###############################################


def remove_duplicates(linked_list):
    if linked_list.head is None:
        return
    node = linked_list.head
    temp_set = set()
    while node.next:
        if node.value not in temp_set:
            temp_set.add(node.value)
        if node.next.value in temp_set:
            if node.next.next is None:
                node.next = None
            else:
                node.next = node.next.next
        else:
            node = node.next
    return linked_list


def get_nth_element(linked_list, n):
    pointer1 = linked_list.head
    pointer2 = linked_list.head

    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.value


def partition(linked_list, value):
    current_node = linked_list.head
    linked_list.tail = linked_list.head
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < value:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node
    if linked_list.tail.next is not None:
        linked_list.tail.next = None


def sum_lists(linked_list, second_linked_list):
    list1 = linked_list.head
    list2 = second_linked_list.head
    carry = 0
    new_list = LinkedList()

    while list1 or list2:
        result = carry
        if list1:
            result += list1.value
            list1 = list1.next
        if list2:
            result += list2.value
            list2 = list2.next
        new_list.add(result % 10)
        carry = result//10
    return new_list


def intersection(first_list, second_list):
    if first_list.tail is not second_list.tail:
        return False

    len_first = len(first_list)
    len_second = len(second_list)

    shorter = first_list if len_first < len_second else second_list
    longer = second_list if len_first < len_second else first_list

    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


first_list = LinkedList()
first_list.add(3)
first_list.add(1)
first_list.add(5)
first_list.add(9)
node1 = Node(7)
node2 = Node(2)
node3 = Node(1)
node1.next = node2
node2.next = node3
first_list.tail.next = node1
first_list.tail = node3
second_list = LinkedList()
second_list.add(2)
second_list.add(4)
second_list.add(6)
second_list.tail.next = node1
second_list.tail = node3
print(first_list)
print(second_list)
new_list = intersection(first_list, second_list)
print(new_list)
