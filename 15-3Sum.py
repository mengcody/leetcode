class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """
        双指针
        :param nums:
        :return:
        """
        nums.sort()  # 排序
        result = []

        for i in range(len(nums) - 2):
            # 跳过最外层重复的
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的元素值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.three_sum(nums))
