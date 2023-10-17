"""
将一个有序数组转为平衡二叉搜索树
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sorted_array_to_array(self, nums) -> TreeNode | None:
        if not nums:
            return None
        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_array(nums[:mid])
        root.right = self.sorted_array_to_array(nums[mid + 1:])

        return root
