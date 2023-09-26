class Solution:
    def min_sub_array_len(self, target: int, nums: list[int]):
        """
        滑动窗口
        :param target:
        :param nums:
        :return:
        """
        if not nums:
            return 0

        min_length = float("inf")
        current_sum = 0

        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    solution = Solution()

    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    assert 2 == solution.min_sub_array_len(target, nums)
