"""
一个数组中没有出现的最小正整数O(n), 空间复杂度为常数级别的

单元素问题

技巧

"""


class Solution:
    def first_missing_positive(self, nums):
        n = len(nums)
        # 首先将非正整数和大于n的数替换为1（假设我们要找的最小正整数一定在1到n+1范围内）
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        print(nums)
        # 标记已经出现的数, 将对应位置的数标记为负数
        for i in range(n):
            num = abs(nums[i])
            if num == n:
                nums[0] = -abs(nums[0])
            else:
                nums[num] = -abs(nums[num])

        print(nums)
        # 找到第一个非负数，该数的下标就是缺失的最小正整数
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # 如果数组中都是正数，缺失的是n+1
        if nums[0] > 0:
            return n

        return n + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 4, -1, 1]
    assert 2 == solution.first_missing_positive(nums)
