from QueueLinkedList import Node, Queue


class AvlNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


def pre_order_traversal(root_node):
    if not root_node:
        return None
    print(root_node.data)
    pre_order_traversal(root_node.left)
    pre_order_traversal(root_node.right)


def in_order_traversal(root_node):
    if not root_node:
        return None
    in_order_traversal(root_node.left)
    print(root_node.data)
    in_order_traversal(root_node.right)


def post_order_traversal(root_node):
    if not root_node:
        return None
    post_order_traversal(root_node.left)
    post_order_traversal(root_node.right)
    print(print(root_node.data))


def level_order_traversal(root_node):
    if not root_node:
        return None

    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        print(root.value.data)
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)


def search(root_node, node_value):
    if not root_node:
        return False
    if root_node.data == node_value:
        return True
    elif root_node.data > node_value:
        if root_node.left.data == node_value:
            return True
        else:
            search(root_node.left, node_value)
    else:
        if root_node.right.data == node_value:
            return True
        else:
            search(root_node.right, node_value)


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def right_rotation(root_node):

    new_root = root_node.left
    root_node.left = root_node.left.right
    new_root.right = root_node
    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root


def left_rotation(root_node):
    new_root = root_node.right
    root_node.right = root_node.right.left
    new_root.left = root_node
    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root


def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left) - get_height(root_node.right)


def insert_node(root_node, node_value):
    if not root_node:
        return AvlNode(node_value)
    if node_value < root_node.data:
        root_node.left = insert_node(root_node.left, node_value)
    else:
        root_node.right = insert_node(root_node.right, node_value)
    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))

    balance = get_balance(root_node)
    if balance > 1:
        if node_value < root_node.left.data:
            return right_rotation(root_node)
        root_node.left = left_rotation(root_node.left)
        return right_rotation(root_node)
    elif balance < -1:
        if node_value > root_node.right.data:
            return left_rotation(root_node)
        root_node.right = right_rotation(root_node.right)
        return left_rotation(root_node)
    return root_node


def get_min_value_node(root_node):
    if root_node is None or root_node.left is None:
        return root_node
    return get_min_value_node(root_node.left)


def delete_node(root_node, node_value):
    if not root_node:
        return root_node
    if node_value < root_node.data:
        root_node.left = delete_node(root_node.left, node_value)
    elif node_value > root_node.data:
        root_node.right = delete_node(root_node.right, node_value)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp
        elif root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp
        temp = get_min_value_node(root_node.right)
        root_node.data = temp.data
        root_node.right = delete_node(root_node.right, temp.data)

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    balance = get_balance(root_node)
    if balance > 1:
        if get_balance(root_node.left) >= 0:
            return right_rotation(root_node)
        root_node.left = left_rotation(root_node.left)
        return right_rotation(root_node)
    elif balance < -1:
        if get_balance(root_node.right) <= 0:
            return left_rotation(root_node)
        root_node.right = right_rotation(root_node.right)
        return left_rotation(root_node)
    return root_node


def delete_avl(root_node):
    if not root_node:
        return None
    root_node.data = None
    root_node.left = None
    root_node.right = None


avl = AvlNode(16)
avl = insert_node(avl, 12)
avl = insert_node(avl, 10)
avl = insert_node(avl, 15)
avl = insert_node(avl, 20)
avl = insert_node(avl, 1)
avl = insert_node(avl, 19)
avl = insert_node(avl, 18)
avl = insert_node(avl, 13)
avl = insert_node(avl, 24)
avl = delete_node(avl, 16)
level_order_traversal(avl)
