# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:

        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def reverse(head: ListNode, k: int) -> ListNode:
            prev = None
            cur = head

            for i in range(k):
                # 辅助变量
                next = cur.next
                # 逆序cur
                cur.next = prev
                # 向前走，准备下一轮
                prev = cur
                cur = next

            return prev

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # 计算应该反转几个, 找这一组中反转开始和结束的点
        length = get_length(head)
        while length >= k:
            group_start = prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            # 记录下下一组的起点
            next_group_start = group_end.next
            # 断开和下一组的关联
            group_end.next = None

            # 反转
            reversed_group_start = reverse(group_start, length)
            # 将上一组和这一组关联起来
            prev.next = reversed_group_start
            # 将这一组和下一组关联起来
            group_start.next = next_group_start

            # 更新
            prev = group_start
            length -= k

        return dummy.next
