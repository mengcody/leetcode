"""
求一个数组的全排列

数组的特征：可能有重复元素
"""


class Solution:
    def permute_unique(self, nums):
        def backtrack(path, used):
            # 全排列的元素个数与数组中元素的个数相同, 找到了一个排列
            if len(path) == len(nums):
                results.append(path[:])
                return results

            # 横向上扫描
            for i in range(len(nums)):
                # 如果元素已经使用过了，或者是重复元素并且前一个相同的元素未被使用过
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                used[i] = False
                path.pop()

        nums.sort()
        results = []
        used = [False] * len(nums)
        print(used)
        backtrack([], used)
        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.permute_unique(nums))
