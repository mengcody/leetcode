class Solution:
    """
    solution1:
    """
    # def reverse_words(self, s):
    #     return " ".join(s.split()[::-1])

    """
    solution2
    1. 先逆序整个字符串
    2. 然后在逆序单个单词
    """

    def reverse_words(self, s):
        s = self._reverse(s)
        ans = []
        for w in s.split():
            w = self._reverse(w)
            ans.append(w)
        return " ".join(ans)

    def _reverse(self, s):
        ans = [''] * len(s)
        if len(s) == 0:
            return
        start = 0
        end = len(s) - 1
        while start <= end:
            ans[start], ans[end] = s[end], s[start]

            start += 1
            end -= 1
        return "".join(ans)


if __name__ == '__main__':
    solution = Solution()
    s = "the sky is blue"
    assert "blue is sky the" == solution.reverse_words(s)
