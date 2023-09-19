class Solution:
    """
    使用两个列表 val 和 syb 来分别存储罗马数字字符和对应的整数值。
    然后，我们通过不断地将整数值减去最大可能的罗马数字值，构建了罗马数字表示。
    通过重复这个过程，我们逐步减小整数值，直到它变为零，同时构建了正确的罗马数字表示。
    """

    # def int_to_roman(self, num: int) -> str:
    #     val = [
    #         1000, 900, 500, 400,
    #         100, 90, 50, 40,
    #         10, 9, 5, 4, 1
    #     ]
    #     syb = [
    #         "M", "CM", "D", "CD",
    #         "C", "XC", "L", "XL",
    #         "X", "IX", "V", "IV",
    #         "I"
    #     ]
    #     roman_numeral = ''
    #     i = 0
    #     # i 为罗马数字值val的索引
    #     while num > 0:
    #         # for 循环的主要目的是将整数值 num 分解成罗马数字的组成部分。
    #         # 循环的条件是 num 大于 0，意味着只要还有整数值需要转换，循环就会继续执行。
    #         i_ = num // val[i]
    #         for _ in range(i_):
    #             roman_numeral += syb[i]
    #             num -= val[i]  # 整数值，减去最大可能的罗马数字
    #         i += 1
    #     return roman_numeral

    def int_to_roman(self, num: int) -> str:
        """
        贪心算法
        从最大的罗马数字开始，尽量多地使用该罗马数字，然后减去对应的整数值。循环过程中，罗马数字逐步构建，直到整数值变为零
        :param num:
        :return:
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman_numeral = ''
        i = 0

        while num > 0:
            if num >= val[i]:
                num = num - val[i]
                roman_numeral += syb[i]
            else:
                i += 1

        return roman_numeral


if __name__ == '__main__':
    solution = Solution()
    num = 3
    assert "III" == solution.int_to_roman(num)
