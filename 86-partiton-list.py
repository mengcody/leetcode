# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        基本思路：x将链表分成了两部分，找到第一部分的头和尾和第二部分的头和尾就可以了
        然后在遍历的时候，看看是将当前遍历到的这个节点放到哪一部分里
        """
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head

        cur = head
        while cur:

            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next

            cur = cur.next

        less.next = greater_head.next
        greater.next = None

        return less_head.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    Solution().partition(head, 3)
