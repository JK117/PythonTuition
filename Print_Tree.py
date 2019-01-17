from collections import namedtuple

# Define the node structure
Node = namedtuple('Node', ['data', 'left', 'right'])

# Initialize the tree
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def function(root):
    A = []
    result = []
    if not root:
        return result
    A.append(root)
    while A:
        current_root = A.pop(0)
        result.append(current_root.val)
        if current_root.left:
            A.append(current_root.left)
        if current_root.right:
            A.append(current_root.right)
    return result

# def level_order_traversal()
