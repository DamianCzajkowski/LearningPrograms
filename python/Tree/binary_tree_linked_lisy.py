from python.Queue.queue_linked_list import Queue


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
        print(root_node.data)
        if root.value.left is not None:
            custom_queue.enqueue(root.value.left)
        if root.value.right is not None:
            custom_queue.enqueue(root.value.right)


root = TreeNode('Drinks')
left = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
left.left = tea
left.right = coffee
right = TreeNode('Cold')
root.left = left
root.right = right


if __name__ == "__main__":
    pre_order_traversal(root)
    print("-"*20)
    in_order_traversal(root)
    print("-"*20)
    post_order_traversal(root)
    print("-"*20)
    level_order_traversal(root)
