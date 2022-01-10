class Node:

    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert_string(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if not node:
                node = Node()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True

    def search(self, word):
        current = self.root

        for ch in word:
            node = current.children.get(ch)
            if not node:
                return False
            current = node

        return current.end_of_string


def delete_string(root,  word, index=0):
    ch = word[index]
    current_node = root.children.get(ch)
    can_be_deleted = False

    if len(current_node.children) > 1:
        delete_string(current_node, word, index+1)
        return False

    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True

    if current_node.end_of_string:
        delete_string(current_node, word, index+1)
        return False

    can_be_deleted = delete_string(current_node, word, index+1)
    if can_be_deleted:
        root.children.pop(ch)
        return True
    return False


trie = Trie()
trie.insert_string("App")
trie.insert_string("Appl")
print(trie.search("App"))
delete_string(trie.root, "App")
print(trie.search("App"))
print(trie.search("Appl"))
