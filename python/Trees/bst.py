from QueueLinkedList import Queue


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root_node, value):
    if root_node.value is None:
        root_node.value = value
    elif root_node.value < value:
        if root_node.right is None:
            root_node.right = Node(value)
        else:
            insert(root_node.right, value)
    else:
        if root_node.left is None:
            root_node.left = Node(value)
        else:
            insert(root_node.left, value)


def pre_order_traversal(root_node):
    if not root_node:
        return None
    print(root_node.value)
    pre_order_traversal(root_node.left)
    pre_order_traversal(root_node.right)


def in_order_traversal(root_node):
    if not root_node:
        return None
    in_order_traversal(root_node.left)
    print(root_node.value)
    in_order_traversal(root_node.right)


def post_order_traversal(root_node):
    if not root_node:
        return None
    post_order_traversal(root_node.left)
    post_order_traversal(root_node.right)
    print(print(root_node.value))


def level_order_traversal(root_node):
    if not root_node:
        return None

    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        print(root.value.value)
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)


def search(root_node, node_value):
    if not root_node:
        return False
    if root_node.value == node_value:
        return True
    elif root_node.value > node_value:
        if root_node.left.value == node_value:
            return True
        else:
            search(root_node.left, node_value)
    else:
        if root_node.right.value == node_value:
            return True
        else:
            search(root_node.right, node_value)


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root_node, value):
    if root_node is None:
        return
    if value < root_node.value:
        root_node.left = delete_node(root_node.left, value)
    elif value > root_node.value:
        root_node.right = delete_node(root_node.right, value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp
        if root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp

        temp = min_value_node(root_node.right)
        root_node.value = temp.value
        root_node.right = delete_node(root_node.right, temp.value)
    return root_node


def delete_tree(root_node):
    if not root_node:
        return None
    root_node.value = None
    root_node.left = None
    root_node.right = None


bst = Node(70)
insert(bst, 50)
insert(bst, 90)
insert(bst, 30)
insert(bst, 60)
insert(bst, 80)
insert(bst, 100)
insert(bst, 20)
insert(bst, 40)
insert(bst, 20)
insert(bst, 85)
insert(bst, 85)
insert(bst, 88)
delete_node(bst, 70)
level_order_traversal(bst)
