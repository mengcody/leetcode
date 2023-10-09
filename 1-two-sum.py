class Solution:
    def two_sum(self, nums, target):
        """
        1. 离散多元素问题
        1.1 先思考暴力解法
        1.2 看看如何加速暴力解答
            a. 先对数据进行预处理，是否能加速
            b. 多指针
        """
        # 1. 暴力：两次遍历
        # return self._solution1(nums, target)
        # 2. 先预处理进行排序，使用双指针加速, 排序之后，数组下表就变了, 不可行
        # return self._solution2(nums, target)
        # 3. 哈希表加速
        return self._solution3(nums, target)

    def _solution1(self, nums, target):
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if a + b == target:
                    return [i, j]

    def _solution2(self, nums, target):
        nums.sort()
        print(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    def _solution3(self, nums, target):
        my_hash = {}
        for i, e in enumerate(nums):
            need = target - e
            if need in my_hash:
                return [my_hash[need], i]
            my_hash[e] = i


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 3]
    target = 6

    print(solution.two_sum(nums, target))
