class BinaryTree:

    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_id = 0
        self.max_size = size

    def __str__(self):
        return "".join(str(self.custom_list[1:self.last_used_id+1]))

    def insert(self, value):
        if self.last_used_id + 1 == self.max_size:
            return "Tree is full"
        self.custom_list[self.last_used_id + 1] = value
        self.last_used_id += 1
        return "Success"

    def search(self, value):
        for idx, item in enumerate(self.custom_list[1:self.last_used_id+1]):
            if item == value:
                return idx + 1
        return None

    def pre_order_traversal(self, index):
        if index > self.last_used_id:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)

    def in_order_traversal(self, index):
        if index > self.last_used_id:
            return
        self.in_order_traversal(index*2)
        print(self.custom_list[index])
        self.in_order_traversal(index*2 + 1)

    def post_order_traversal(self, index):
        if index > self.last_used_id:
            return
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2 + 1)
        print(self.custom_list[index])

    def level_order_traversal(self):
        for item in self.custom_list[1:self.last_used_id+1]:
            print(item)

    def delete_node(self, value):  # this is ugly
        if self.last_used_id == 0:
            return "Empty"
        for idx, item in enumerate(self.custom_list[1:self.last_used_id+1]):
            if item == value:
                self.custom_list[idx] = self.custom_list[self.last_used_id]
                self.custom_list[self.last_used_id] = None
                self.last_used_id -= 1
                return "Success"

    def delete_tree(self):
        self.custom_list = self.max_size * [None]
        self.last_used_id = 0


bt = BinaryTree(8)
bt.insert("Drinks")
bt.insert("Hot")
bt.insert("Cold")
print(bt)
print(bt.search("Cold"))
