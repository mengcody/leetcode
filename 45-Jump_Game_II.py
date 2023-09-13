class Solution:
    def jump_game(self, nums: list[int]) -> int:
        n = len(nums)
        max_reach = 0
        steps = 0
        curr_end = 0
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_end:
                step += 1
                curr_end = max_reach

                if curr_end >= n - 1:
                    break
        return steps


if __name__ == "__main__":
    pass
