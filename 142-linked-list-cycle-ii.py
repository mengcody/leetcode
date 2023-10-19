# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        has_circle = False
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_circle = True
                break

        if not has_circle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
