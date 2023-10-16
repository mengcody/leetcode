"""
题目要求生成所有可能的二叉搜索树（BST），即给定一个整数 n，生成所有包含 1 到 n 的节点，且每个节点都是二叉搜索树根节点的二叉搜索树。


------------

从1-n的每个值i，都可以作为根节点：它的左子树为[1, i-1], 右子树为[i+1, n]

然后左子树还可以是  从[1, i-1]中的每个值j，都可以作为根节点: 左子树为[1,j-1], 右子树为[j+1, i-1]
..........

----------
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def generate_trees(self, n: int):
        if not n:
            return []

        return self._generate(1, n)

    def _generate(self, start, end):
        """
        1. 定义函数的作用：给定一个区间范围，返回这些数字可以组成的的所有可能的二叉搜索树
        """
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = self._generate(start, i - 1)
            right_trees = self._generate(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = left
                    current_tree.right = right
                    all_trees.append(current_tree)

        return all_trees


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate_trees(4))
