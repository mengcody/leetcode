from collections import Counter


class Solution:
    def find_sub_strings(self, s: str, words: list[str]) -> list[int]:
        """
        words 串联起来，可以任意顺序组成一个字符串
        这个字符串是s的子串
        返回子串，索引开始位置

        我们使用滑动窗口的思想，遍历字符串，每次取固定长度的子串，并检查是否符合给定的单词组合。
        根据单词长度，进行滑动窗口的移动。最终返回符合条件的子串的起始索引。
        """
        if not s and not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        result = []

        words_freq = Counter(words)  # Counter({'a': 3, 'b': 4})

        # 开始遍历
        for i in range(word_len):
            left = right = i
            window = Counter()  # 统计子串中每个单词出现的次数

            # 构建可能符合条件的子串
            # 每个可能的子串的长度应该是 words 中所有单词拼接的长度，所以我们每次移动的步长是一个单词的长度。
            while right + word_len <= len(s):
                # 取固定长度的子串, 然后判断是否符合给定单词的组合
                # right 向前走，同时将自己长度的单词，放到字典中统计
                word = s[right : right + word_len]
                right += word_len
                window[word] += 1

                # 检查当前子串是否符合条件
                # left 移动，碰到一个抵消一个
                while window[word] > words_freq[word]:
                    window[s[left : left + word_len]] -= 1
                    left += word_len
                if right - left == total_len:
                    result.append(left)

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(solution.find_sub_strings(s, words))
