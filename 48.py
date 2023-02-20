class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def morris_inorder(root):
    current = root
    while current is not None:
        if current.left is None:
            yield current.val
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                yield current.val
                current = current.right


one = TreeNode(1, None, None)
three = TreeNode(3, None, None)
two = TreeNode(2, one, three)
five = TreeNode(5, None, None)
seven = TreeNode(7, None, None)
six = TreeNode(6, five, seven)
four = TreeNode(4, two, six)

for node in morris_inorder(four):
    print(node)
