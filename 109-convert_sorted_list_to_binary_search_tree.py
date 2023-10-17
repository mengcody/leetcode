"""
将一个有序链表转为二叉树搜索树
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_list_to_BST(self, head: ListNode):
        if not head:
            return None

        # slow       ---->  root
        # head       ---->  root.left 的第一个节点
        # slow.next  ---->  root.right 的第一个节点

        slow, fast = head, head
        prev_slow = None

        # 先走到合适的位置
        # slow 走到中间
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        # 如果只有一个节点 在List中
        if prev_slow:
            prev_slow.next = None  # 断开和root的联系
            # 构建左子树
            root.left = self.sorted_list_to_BST(head)
        else:
            root.left = None
        # 构建右子树
        root.right = self.sorted_list_to_BST(slow.next)

        return root


if __name__ == '__main__':
    pass
