# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        """
        层序遍历二叉搜索树，使用队列
        """
        if not root:
            return []
        queue = deque([root])

        result = []
        while queue:
            level = []
            level_size = len(queue)  # 每一层的元素个数
            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result
