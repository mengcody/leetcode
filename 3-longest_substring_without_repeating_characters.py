class Solution:
    def length_of_longest_sub_string(self, s):
        if not s:
            return 0

        max_length = 0
        char_to_index = {}  # 保存字符，对应的位置
        start = 0

        for end in range(len(s)):
            if s[end] in char_to_index and char_to_index[s[end]] >= start:
                start = char_to_index[s[end]] + 1

            char_to_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    assert 3 == solution.length_of_longest_sub_string(s)
