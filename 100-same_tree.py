"""
判断两棵树是不是一样的
"""


class Solution:

    def isSameTree(self, p, q) -> bool:

        def pre_order(root):
            if not root:
                return [None]

            result = []

            result.append(root.val)
            result += pre_order(root.left)
            result += pre_order(root.right)

            return result

        a = pre_order(p)

        b = pre_order(q)

        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True
