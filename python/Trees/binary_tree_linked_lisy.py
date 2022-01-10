from QueueLinkedList import Queue


class TreeNode:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


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
    print(root_node.data)


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
        return None
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.data == node_value:
            return "OH yEs!"
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)
    return "Not found"


def insert(root_node, new_node):
    if not root_node:
        root_node = new_node
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        else:
            root.value.left = new_node
            return
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)
        else:
            root.value.right = new_node
            return


def get_deepest_node(root_node):
    if not root_node:
        return None
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)
    deepest_node = root.value
    return deepest_node


def delete_deepest_node(root_node, d_node):
    if not root_node:
        return None
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value is d_node:
            root.value = None
            return
        if root.value.right:
            if root.value.right is d_node:
                root.value.right = None
                return
            custom_queue.enqueue(root.value.right)
        if root.value.left:
            if root.value.left is d_node:
                root.value.left = None
                return
            custom_queue.enqueue(root.value.left)


def delete_node(root_node, node):
    if not root_node:
        return None
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.data == node:
            d_node = get_deepest_node(root_node)
            root.value.data = d_node.data
            delete_deepest_node(root_node, d_node)
            return "Success"
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)
    return "Failed"


def delete_tree(root_node):
    if not root_node:
        return None
    root_node.data = None
    root_node.left = None
    root_node.right = None


root = TreeNode("Drinks")
left = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
left.left = tea
left.right = coffee
right = TreeNode("Cold")
root.left = left
root.right = right
new_node = TreeNode("NO DATA")

if __name__ == "__main__":
    pre_order_traversal(root)
    print("-" * 20)
    in_order_traversal(root)
    print("-" * 20)
    post_order_traversal(root)
    print("-" * 20)
    level_order_traversal(root)
    print("-" * 20)
    print(search(root, "Coffee"))
    print("-" * 20)
    insert(root, new_node)
    level_order_traversal(root)
    deepest_node = get_deepest_node(root)
    print("-" * 20)
    print(deepest_node.data)
