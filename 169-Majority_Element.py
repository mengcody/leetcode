class Solution:
    def majority_element(self, nums: list[int]) -> int:
        # travse the array, when meet the element what action should you do?
        count = dict()
        for n in nums:
            if count.get(n) is not None:
                count[n] = count[n] + 1
            else:
                count[n] = 1

        return max(count, key=count.get)



if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    a = solution.majority_element(nums)
    print(a)
