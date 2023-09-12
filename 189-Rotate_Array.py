class Solution:
    def rotate_array(self, nums: list[int], k: int) -> list[int]:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # reverse two times
    # 1. reverse all element 
    # 2. reverse the last k element
    
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate_array(nums, 3)
    pass
