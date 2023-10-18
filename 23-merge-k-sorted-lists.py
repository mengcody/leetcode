"""
合并k个有序的链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: list[[ListNode]]) -> ListNode:
        def sorted_list(l: list[[ListNode]]) -> list:
            result = []
            for i in range(len(lists)):
                cur = lists[i]
                values = []
                while cur:
                    values.append(cur.val)
                    cur = cur.next
                result += sorted(values)
            return result

        dummy = ListNode()
        cur = dummy

        a = sorted_list(lists)

        for v in a:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next
