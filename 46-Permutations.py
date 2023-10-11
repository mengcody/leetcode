"""
全排列
"""


class Solution:
    def premute(self, nums):
        def backtrack(start):
            # 终止条件
            if start == len(nums):
                result.append(nums[:])
                return result

            for i in range(start, len(nums)):
                # 选择 # 将当前位置与起始位置交换，固定该位置的元素
                nums[start], nums[i] = nums[i], nums[start]
                # 递归
                backtrack(start + 1)
                # 回溯
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.premute(nums))
