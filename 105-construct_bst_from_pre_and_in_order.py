"""
从前序，中序 构建二叉树

构建树：
1. 找根节点
2. 构建左子树
3. 构建右子树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, pre_order: list[int], in_order: list[int]) -> TreeNode | None:
        if not pre_order or not in_order:
            return None
        # 前序遍历的第一个节点是树的根
        root_val = pre_order.pop(0)
        root = TreeNode(root_val)

        # 在中序遍历中找root的下标索引是多少
        root_index = in_order.index(root_val)

        root.left = self.build_tree(pre_order, in_order[:root_index])
        root.right = self.build_tree(pre_order, in_order[root_index + 1:])
        return root
