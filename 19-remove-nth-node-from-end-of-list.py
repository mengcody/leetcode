"""
移除链表的倒数第k个节点

先fast到k步
然后，slow和fast同时走，当fast到终点的时候，slow刚好到 要删除节点的前一个节点

1.
  head  ----> 1 ----> 2 ----> 3 ----> 4 ----> 5
  |
 slow
 fast

2.  fast 先走 n + 1
  head  ----> 1 ----> 2 ----> 3 ----> 4 ----> 5
  |                           |
 slow                        fast

3. 同时走，到fast为none
  head  ----> 1 ----> 2 ----> 3 ----> 4 ----> 5 ----> None
                             |                        |
                            slow                     fast

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

    def remove_nth_from_end2(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    # solution.remove_nth_from_end(head, 2)
    #
    # cur = head
    # while cur:
    #     print(cur.val)
    #     cur = cur.next
    solution.remove_nth_from_end(head, 2)

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
