"""
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。

这个算法首先从右向左找到第一个递减的元素，即 nums[i] < nums[i+1] 的位置。
如果找到了这样的元素，再从右向左找到第一个大于 nums[i] 的元素，并交换它们。
最后，将 nums[i+1:] 部分翻转，得到下一个排列。

如果找不到递减元素，说明数组已经是最大排列，直接将数组翻转得到最小排列。
"""


class Solution:
    def next_permutation(self, nums):
        # 从右向左找递减的元素
        n = len(nums)

        # Find the first decreasing element from right to left
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest element greater than nums[i] to its right
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements to the right of nums[i]
        self.reverse(nums, i + 1, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.next_permutation(nums)
    assert [1, 3, 2] == nums

    nums = [2, 3, 1]
    solution.next_permutation(nums)
    assert [3, 1, 2] == nums
