class Solution:
    def max_profit(self, nums: list[int]) -> int:
        # travse
        # max_profit = 0

        # for i, n in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] - n > max_profit:
        #             max_profit = nums[j] - n

        # return max_profit

        min = float('inf')
        max_profix = 0
        for p in nums:
            if p < min:
                min = p

            if p - min > max_profix:
                max_profix = p - min

        return max_profix


if __name__ == "__main__":
    solution = Solution()
    nums = [7, 1, 5, 3, 6, 4]
    print(solution.max_profit(nums))
