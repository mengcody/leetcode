class Solution:
    def length_of_last_word(self, s: str) -> int:
        """

        逆序遍历
        1. 逆序的时候，第一个即使空格
        2. 逆序的死后，第一个不是空格

        :param s:
        :return:
        """
        last_length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                last_length += 1
            else:
                if last_length > 0:
                    return last_length

        return last_length


if __name__ == '__main__':
    solution = Solution()
    s = "luffy is still joyboy"
    assert 6 == solution.length_of_last_word(s)
