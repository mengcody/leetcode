"""
二叉树层序遍历
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = [root]
        result = []
        while queue:
            level_val = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop()
                level_val.append(node.val)

                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)

            result.insert(0, level_val)
        return result
