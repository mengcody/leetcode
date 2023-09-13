class Solution:
    def jump_game(self, nums: list[int]) -> bool:
        # greedy algorithm
        # greedy policy is: 遍历，获取 从当前位置能到达的最远距离
        n = len(nums)
        farthest = 0  # represent the farthest position we can reach at i positon
        for i in range(n):
            # i represent the current position
            # 如果能到达的最远距离，小于当前位置
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.jump_game()
