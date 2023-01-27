class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def append(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return
        else:
            current = self.root_node
            parent = None

            while True:
                parent = current
                if current.data < node.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
                else:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current.data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current.data

    def inorder_traversal(self, root_node, arr):
        if root_node is None:
            return
        else:
            self.inorder_traversal(root_node.left_child, arr)
            arr.append(root_node.data)
            self.inorder_traversal(root_node.right_child, arr)

        return arr
    
    def print_tree(self):
        print(f"Tree: {self.inorder_traversal(tree.root_node, [])}")

    def delete_node(self, data):
        current = self.root_node
        if self.root_node is None:
            return
        while current:
            if current.data > data:
                current = current.left_child
                if current.data == data:
                    current.left_child = None
                    return
            else:
                current = current.right_child
                if current.data:
                    current.right_child = None
                    return


tree = Tree()
nums = [23, 12, 31, 16, 11, 7]
[tree.append(num) for num in nums]
tree.print_tree()
print(f"Maximum: {tree.find_max()}")
print(f"Minimum: {tree.find_min()}")

