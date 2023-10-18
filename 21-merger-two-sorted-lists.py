class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merger_two_lists(self, head1: ListNode | None, head2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        while head1 and head2:
            if head1.val < head2.val:
                node = ListNode(head1.val)
                cur.next = node
                head1 = head1.next
            else:
                node = ListNode(head2.val)
                cur.next = node
                head2 = head2.next
            cur = cur.next

        cur.next = head1 if head1 else head2
        return dummy.next
