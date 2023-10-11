class Solution:
    def combination_sum2(self, candidates, target):
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # 去掉重复的
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 先排序，就可以用这个条件进行剪枝了
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i+1, target - candidates[i], path, result)
                path.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [], result)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solution.combination_sum2(nums, target))
