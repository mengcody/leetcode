"""
一个二叉搜索树中有两个节点位置搞错了，给他纠正过来
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 记录当前遍历的节点的上一
        self.first_node = None  # 需要交换的节点1
        self.second_node = None  # 需要交换的几点2

        # 记录前一个访问的节点的变量
        self.pre_node = TreeNode(float('-inf'))

        # 中序遍历
        def in_order(root):
            if not root:
                return

            in_order(root.left)

            if self.first_node is None and self.pre_node.val >= root.val:
                self.first_node = self.pre_node
            if self.first_node and self.pre_node.val >= root.val:
                self.second_node = root

            self.pre_node = root

            in_order(root.right)

        in_order(root)

        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val


if __name__ == '__main__':
    solution = Solution()
    solution.recover_tree(root)
    pass
