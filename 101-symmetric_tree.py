class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_symmetric_tree(self, root: TreeNode):
        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)
