class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal(self, root: None | TreeNode) -> list[int]:
        """
        递归函数，定义的三要素：
        1. 函数的作用，定义清晰: 给定一个根节点，返回该根节点中序遍历的结果
        2. 函数的参数
        3. 函数的返回值
        """
        if not root:
            return []

        result = []

        result += self.inorder_traversal(root.left)
        result.append(root.value)
        result += self.inorder_traversal(root.right)

        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    root.right = node2
    root.left = None

    node2.right = None
    node2.left = node3

    node3.left = None
    node3.right = None

    print(solution.inorder_traversal(root))
