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

    if root_node is None:
        return []

    yield from traverse_inorder(root_node.left)
    yield root_node.val
    yield from traverse_inorder(root_node.right)


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
    current_node = root_node

    while current_node is not None:

        if current_node.left is None:
            yield current_node.val
            current_node = current_node.right

        else:
            predecessor_node = current_node.left

            while predecessor_node.right is not None and predecessor_node.right is not current_node:
                predecessor_node = predecessor_node.right

            if predecessor_node.right is None:
                predecessor_node.right = current_node
                current_node = current_node.left
            else:
                predecessor_node.right = None
                yield current_node.val
                current_node = current_node.right


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
