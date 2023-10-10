class Solution:
    def search_range(self, nums, target):
        """
        在一个有序的数组中，找目标target第一个位置的下比标和最后一个的下标
        二分查找

        找左边：
        找右边：
        """

        def search_first_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # 继续在左半部分查找第一个出现的位置
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        def search_last_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # 继续在右半部分查找最后一个出现的位置
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        first_occurrence = search_first_occurrence(nums, target)
        last_occurrence = search_last_occurrence(nums, target)
        return [first_occurrence, last_occurrence]


if __name__ == '__main__':
    solution = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    res = solution.search_range(nums, target)
    print(res)
    assert [3, 4] == res
