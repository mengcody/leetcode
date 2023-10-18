class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l3 = ListNode()

        head1 = l1
        head2 = l2
        head3 = l3

        x = 0
        while head1 or head2:
            v = x
            if head1:
                v += head1.val
                head1 = head1.next
            if head2:
                v += head2.val
                head2 = head2.next

            node = ListNode(v % 10)
            head3.next = node
            x = v // 10

            head3 = head3.next
        if x:
            head3.next = ListNode(x)

        return l3.next

    pass


if __name__ == '__main__':
    l1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    l1.next = node2
    node2.next = node3

    l2 = ListNode(5)
    node3 = ListNode(6)
    node4 = ListNode(4)
    l2.next = node3
    node3.next = node4

    res = Solution().add_two_numbers(l1, l2)

    cur = res
    while cur:
        print(cur.val)
        cur = cur.next
