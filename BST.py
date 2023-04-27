from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, value, node=None):
        if not node:
            node = self.root
            if value > node.value:
                if not node.right:
                    node.right = Node(value)
                else:
                    return self.add_node(value, node.right) 
            else:
                if not node.left:
                    node.left = Node(value)
                else:
                    return self.add_node(value, node.left)
    
    def get_min(self, node=None):
        if not node:
            node = self.root
        if node.left:
            return self.get_min(node.left)
        else:
            return node.value

    def get_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value
    
    def contains(self, target):
        current_node = self.root
        while current_node:
            if target == current_node.value:
                return True
            if target > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False

    def print_in_order(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.print_in_order(node.left)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)



bst = BinarySearchTree(100)
bst.add_node(80)
bst.add_node(90)
bst.add_node(70)
bst.add_node(150)
bst.add_node(120)
bst.add_node(110)

print(bst.root.value)
print(bst.get_max())