class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        双指针
        :param s:
        :param t:
        :return:
        """
        ptr_s = 0
        ptr_t = 0
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1

        return ptr_s == len(s)


if __name__ == '__main__':
    solution = Solution()
    s = 'abc'
    t = 'ahbgbc'
    assert True == solution.is_subsequence(s, t)
