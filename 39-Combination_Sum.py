"""
回溯算法
"""


class Solution:
    def combination_sum(self, candidates, target):
        # path 为路径
        # result 为结果
        # target 为每一次的目标值
        def backtrack(start, target, path, result):
            # 递归的终止条件
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                # 选择
                path.append(candidates[i])
                # 递归
                backtrack(i, target - candidates[i], path, result)
                # 回溯
                path.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [], result)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 6, 7]
    tar = 7
    print(solution.combination_sum(nums, tar))
