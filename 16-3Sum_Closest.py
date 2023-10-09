class Solution:
    """
    从一个数组中找三个数，
    这三个数的和 最接近给定的 target
    """

    def three_sum_closest(self, nums, target):
        # 1. 暴力, 数组中的三个数的所有组合
        self._solution1(nums, target)
        # 2. 加速: 先排序，然后双指针
        self._solution2(nums, target)

    def _solution1(self, nums, target):
        res = float("inf")
        min_value = float("inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if abs(sum([nums[i], nums[j], nums[k]]) - target) < min_value:
                        min_value = abs(sum([nums[i], nums[j], nums[k]]) - target)
                        res = sum([nums[i], nums[j], nums[k]])

        return res

    def _solution2(self, nums, target):
        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return closest_sum
        return closest_sum


if __name__ == "__main__":
    solution = Solution()
    nums = [
        -12,
        -44,
        -67,
        -65,
        17,
        17,
        -80,
        73,
        51,
        46,
        -48,
        -43,
        -31,
        17,
        68,
        25,
        79,
        65,
        -41,
        18,
        -68,
        -7,
        29,
        -19,
        -48,
        3,
        -67,
        73,
        -57,
        -90,
        12,
        37,
        -16,
        -1,
        -65,
        47,
        53,
        -79,
        0,
        -62,
        -96,
        -10,
        -79,
        -25,
        38,
        93,
        28,
        6,
        99,
        68,
        -25,
        -27,
        -1,
        -61,
        70,
        -50,
        -54,
        -93,
        43,
        -34,
        31,
        98,
        -56,
        -70,
        44,
        49,
        -52,
        13,
        15,
        55,
        63,
        16,
        -30,
        -15,
        -25,
        87,
        75,
        81,
        19,
        17,
        88,
        -99,
        9,
        -92,
        -52,
        75,
        -16,
        97,
        -99,
        -86,
        60,
        -45,
        -88,
        99,
        75,
        36,
        -82,
        -67,
        -12,
        -47,
        37,
        -44,
        -45,
        67,
        85,
        -32,
        57,
        -11,
        -35,
        -51,
        -25,
        -38,
        54,
        -30,
        96,
        -62,
        -31,
        53,
        -79,
        -19,
        37,
        -73,
        95,
        -38,
        -60,
        72,
        -8,
        -24,
        -46,
        -61,
        63,
        -41,
        95,
        37,
        -79,
        -1,
        74,
        -9,
        92,
        97,
        -34,
        -69,
        -43,
        38,
        79,
        64,
        21,
        68,
        64,
    ]
    target = 189
    print(solution.three_sum_closest(nums, target))
