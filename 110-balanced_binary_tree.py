"""
判断一个二叉树是不是平衡的
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_balances(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def depth(root):
            """
            求树的高度
            """
            if not root:
                return 0
            a = depth(root.left)
            return a

        # 左子树的高度
        left = depth(root.left)
        # 右子树的高度
        right = depth(root.right)

        return abs(left - right) < 2 and self.is_balances(root.left) and self.is_balances(root.right)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    assert True == Solution().is_balances(node1)
