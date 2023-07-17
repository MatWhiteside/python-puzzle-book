from __future__ import annotations
from typing import Iterator


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def traverse_inorder(root_node: TreeNode | None) -> Iterator[int]:
    # Your implementation here


one = TreeNode(1, None, None)
three = TreeNode(3, None, None)
two = TreeNode(2, one, three)
five = TreeNode(5, None, None)
seven = TreeNode(7, None, None)
six = TreeNode(6, five, seven)
four = TreeNode(4, two, six)

for node in traverse_inorder(four):
    print(node)

one = TreeNode(1, None, None)
four = TreeNode(4, None, None)
three = TreeNode(3, None, four)
two = TreeNode(2, one, three)

for node in traverse_inorder(two):
    print(node)

for node in traverse_inorder(None):
    print(node)


# Bonus Solution
def morris_traverse_inorder(root_node: TreeNode | None) -> Iterator[int]:
    # Your implementation here


one = TreeNode(1, None, None)
three = TreeNode(3, None, None)
two = TreeNode(2, one, three)
five = TreeNode(5, None, None)
seven = TreeNode(7, None, None)
six = TreeNode(6, five, seven)
four = TreeNode(4, two, six)

for node in morris_traverse_inorder(four):
    print(node)

one = TreeNode(1, None, None)
four = TreeNode(4, None, None)
three = TreeNode(3, None, four)
two = TreeNode(2, one, three)

for node in morris_traverse_inorder(two):
    print(node)

for node in morris_traverse_inorder(None):
    print(node)
