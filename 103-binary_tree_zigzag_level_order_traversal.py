import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def zigzag_level_order(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        level = 0
        while queue:
            level_data = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                val = node.val
                if level % 2 == 0:
                    level_data.append(val)
                else:
                    level_data.insert(0, val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
            result.append(level_data)

        return result


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

    print(Solution().zigzag_level_order(node1))
