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

    def preorder_traversal(self, root_node, arr):
        if root_node is None:
            return
        else:
            arr.append(root_node.data)
            self.preorder_traversal(root_node.left_child, arr)
            self.preorder_traversal(root_node.right_child, arr)

        return arr

    def print_tree(self):
        print(f"Values of Tree:{self.preorder_traversal(tree.root_node, [])}")


tree = Tree()
nums = [81, 12, 32, 73, 47]
[tree.append(num) for num in nums]
print(tree.print_tree())
