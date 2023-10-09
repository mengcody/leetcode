"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

1. 暴力：合并为1个，然后获取中位数
2. 加速: 使用到了技巧, 中位数是一个或者两个数，这个数左边的数都比他小，右边的数都比他大, 并且这个数在这个数组中间位置

    二分查找来确定如何分割两个数组, 以确保左半部分的元素，小于右半部分的元素

"""


class Solution:
    def find_median_sorted_arrays(self, num1, num2):
        # return self._solution1(num1, num2)
        return self._solution2(num1, num2)

    def _solution1(self, num1, num2):
        """
        暴力
        """
        # 1. 合成1个
        num3 = self._merge(num1, num2)
        print(num3)
        length = len(num3)
        # 2. 求num3的中位数
        if length & 1 == 1:
            return num3[length // 2]
        else:
            return (num3[length // 2] + num3[length // 2 - 1]) / 2
        pass

    def _merge(self, num1, num2):
        num3 = []

        i = 0
        j = 0
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                num3.append(num1[i])
                i += 1
            else:
                num3.append(num2[j])
                j += 1

        while i < len(num1):
            num3.append(num1[i])
            i += 1
        while j < len(num2):
            num3.append(num2[j])
            j += 1
        return num3

    def _solution2(self, num1, num2):
        # 确保num1为较短的那个
        if len(num1) > len(num2):
            return self._solution2(num2, num1)

        x, y = len(num1), len(num2)
        low, high = 0, x  # 以较短的哪个进行处理

        while low < high:
            # partition_x  num1 的分界线下标
            partition_x = (low + high) // 2  # 较短的那个的中间位置

            # partition_y  num2 的分界线
            # partition_x + partition_y = (x + y + 1) // 2
            partition_y = (x + y + 1) // 2 - partition_x  # 较长的那个的中间位置

            # x 左边半的最大值
            max_x = float("-inf") if partition_x == 0 else num1[partition_x - 1]
            # y 左半边的最大值
            max_y = float("-inf") if partition_y == 0 else num2[partition_y - 1]

            # 右半边的最小值
            min_x = float("inf") if partition_x == x else num1[partition_x]
            min_y = float("inf") if partition_y == y else num2[partition_y]

            # 目标：左半边的数据   小于  右半边的数据
            # x 的 左边的最大值 < y 的 右边的最小值
            # y 的 左边的最大值 < x 的 右边的最小值
            if max_x < min_y and max_y <= min_x:
                if (x + y) % 2 == 0:  # 如果为偶数
                    return (max(max_x, max_y) + min(min_x, min_y)) / 2
                else:  # 如果是奇数
                    return max(max_x, max_y)
            elif max_x > min_y:  # 说明x 的 partition 需要减小, 减小high就行
                high = partition_x - 1
            else:
                low = partition_x + 1


if __name__ == "__main__":
    solution = Solution()
    num1 = [1, 3, 4, 9]
    num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution.find_median_sorted_arrays(num1, num2))
