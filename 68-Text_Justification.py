class Solution:
    def full_justify(self, words, max_width):
        result = []
        current_line = []
        current_length = 0

        for word in words:
            # current_length 表示当前行的字符数量, 不包括空格
            # current_line 用来放当前行可以放置的单词
            if current_length + len(word) + len(current_line) > max_width:
                # 还需要几个字符 num_extra_spaces
                num_extra_spaces = max_width - current_length
                if len(current_line) > 1:  # 如果里面有最少两个单词, 把这两个单词用空格连接起来
                    # 需要几个空格，来拼接单词, 因为每个单词之间要一个空格
                    spaces_between_words = num_extra_spaces // (len(current_line) - 1)
                    justified_line = (" " * spaces_between_words).join(current_line)

                    # 额外还需要几个空格
                    extra_spaces = num_extra_spaces % (len(current_line) - 1)
                    justified_line += " " * extra_spaces
                else:  # 如果只有一个单词, 说明这一行只能容纳一个单词，其他的都用空格补齐
                    justified_line = current_line[0] + ' ' * (max_width - current_length)

                # 该处理下一行了
                result.append(justified_line)
                current_line = []
                current_length = 0

            # 如果这一行还能放下
            current_line.append(word)
            current_length += len(word)

        # 遍历完了，最后一样行，还需要处理
        last_line = " ".join(current_line)
        last_line += " " * (max_width - len(last_line))
        result.append(last_line)

        return result


if __name__ == '__main__':
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    print(solution.full_justify(words, max_width))
    pass
