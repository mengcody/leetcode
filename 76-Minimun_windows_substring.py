from collections import Counter

"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
"""


class Solution:
    """
    window中是否包含t中的所有字符：通过比较字符的相同字符的个数来比较

    例如：
        如果t中有3个A，4个B，同时window中也包含3个A，4个B，那么就是ok的
    """

    def min_window(self, s, t):
        if not s or not t:
            return ""

        target_count = Counter(t)  # Counter({'a': 3, 'b': 4}) , 统计字符出现的频次
        required_chars = len(target_count)  # 一共几种字符 ab 两种

        left = right = 0
        formed = 0  # 表示滑动窗口中，字符有几种
        window_count = {}  # char: count

        min_length = float("inf")  # 符合结果的字符串的最小长度
        result = ""

        for right in range(len(s)):
            char = s[right]
            # 更新window_count
            window_count[char] = window_count.get(char, 0) + 1

            # 判断这个字符，是不是组成target需要的
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # 缩小滑动窗口
            while formed == required_chars and left <= right:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right + 1]

                char = s[left]
                window_count[char] -= 1

                # 窗口不能再缩小的条件, 窗口中某个字符的数量 少于 t中需要的字符的数量了
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1

                left += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    assert "BANC" == solution.min_window(s, t)
