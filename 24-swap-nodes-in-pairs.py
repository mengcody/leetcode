# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        cur = head

        # 从头节点开始遍历
        while cur and cur.next:
            # 使用两个临时变量
            first_node = cur
            second_node = cur.next

            # 交换位置
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # 向前走
            cur = first_node.next
            prev = first_node

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)

    head.next = node1
    node1.next = node2
    node2.next = node3

    a = Solution().swapPairs(head)

    cur = a
    while cur:
        print(cur.val)
        cur = cur.next
