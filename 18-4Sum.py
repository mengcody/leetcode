class Solution:
    def four_sum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[right], nums[left]])

                        # 跳过重复的数
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 2, 2, 2]
    target = 8
    print(solution.four_sum(nums))
