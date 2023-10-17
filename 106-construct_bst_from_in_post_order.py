"""
从 中序，后序  构建二叉树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        i = inorder.index(root_val)

        root.left = self.buildTree(inorder[:i], postorder)
        root.right = self.buildTree(inorder[i + 1:], postorder)

        return root
