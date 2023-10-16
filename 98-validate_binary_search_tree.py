"""
判断一个树是不是二叉搜索树

常用方法是通过中序遍历二叉树，如果遍历结果是升序的，则该二叉树是二叉搜索树。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def is_valid_BST(self, root):
        """
        根据左子树大于右子树这个特点
        """
        result = self._traverse(root)
        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False

        return True

    def _traverse(self, root):
        if not root:
            return []

        result = []
        result += self._traverse(root.left)
        result.append(root.val)
        result += self._traverse(root.right)
        return result


if __name__ == '__main__':
    pass
