"""
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

单元素问题
    * 判断一个数组中，是否存在某个数 O(log(n))
"""


class Solution:
    def search(self, nums, target):
        """
        二分查找的变种: 主要思路是根据旋转数组的特性，通过比较中间元素与两边的元素，来确定哪一部分是有序的，然后在有序的这个里面使用二分查找

         mid
         left
         target
         right
         四个数进行比较，确定 left和right如何移动
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 判断哪一部分是有序的
            if nums[left] <= nums[mid]:  # 说明左边部分是有序的
                # 判断目标值在哪边
                if nums[left] <= target <= nums[mid]:  # 目标值在左边
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右边是有序的
                if nums[mid] <= target <= nums[right]:  # 目标值在右边
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert 4 == solution.search(nums, target)
