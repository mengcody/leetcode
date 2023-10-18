# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        # 重复元素的前一个元素
        prev = dummy
        cur = head

        while cur:
            # 跳过重复的
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # 更新prev，是否需要向前走
            if prev.next == cur:  # 相等说明cur没有走
                prev = prev.next
            else:  # prev指向不重复的下一个节点
                prev.next = cur.next

            cur = cur.next
        return dummy.next
