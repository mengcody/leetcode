class Solution:
    def max_profit(self, nums: list[int]) -> int:
        # greedy algorithm
        total_profit = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                total_profit += nums[i + 1] - nums[i]
        return total_profit


if __name__ == "__main__":
    solution = Solution()
    nums = [7, 1, 5, 3, 6, 4]

    print(solution.max_profit(nums))
