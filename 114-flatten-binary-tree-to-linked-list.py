# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        使用栈对遍历
        """
        if not root:
            return

        stack = [root]

        # 指向"新"树的节点, 遍历的过程成一步步的移动到下一个节点
        prev = None

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if prev:
                prev.left = None
                prev.right = node

            prev = node


if __name__ == '__main__':
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    # Flatten the tree to a linked list
    Solution().flatten(root)

    # Print the linked list
    while root:
        print(root.val, end=" -> ")
        root = root.right
