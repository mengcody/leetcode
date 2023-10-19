"""
# Definition for a Node.

使用层序遍历，是最后一个的时候先取出来，在放回去
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = [root]

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop()
                if i == length - 1:
                    node.next = None
                else:
                    node_next = queue.pop()
                    node.next = node_next
                    queue.append(node_next)

                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)

        return root


if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    # Populate next pointers
    Solution().connect(root)
