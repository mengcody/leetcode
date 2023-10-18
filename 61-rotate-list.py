# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        size = 0
        while cur.next:
            size += 1
            cur = cur.next

        if not k % size:
            return head

        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    Solution().rotateRight(head, 2)
