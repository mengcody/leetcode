# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """"""
        if not head or not head.next:
            return head

        # Step 1: Split the linked list into two halves
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 分成两部分
        first_half = head
        second_half = slow.next

        slow.next = None

        # Step 2: Reverse the second half
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half = prev

        # Step 3: Merge the two halves alternately
        while second_half:
            next_first = first_half.next
            next_second = second_half.next
            first_half.next = second_half
            second_half.next = next_first
            first_half = next_first
            second_half = next_second

        return head
