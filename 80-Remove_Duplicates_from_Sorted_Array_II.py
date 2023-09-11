class Solution:
    """
    把一个数组，看成两个数组，一个新的数组，一个当前需要遍历的数组，
    * 遍历旧数组，判断当前遍历到的元素，能不能放到新的数组中
    """
    def remove_duplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # index 指向新数组的位置
        index = 2
        
        # i 遍历数组
        for i in range(2, len(nums)):
            # 检查是否与新数组中的前两个元素相同
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1
        
        print(nums[:index])
        return index



if __name__ == "__main__":
    solution = Solution()
    # nums = [1,1,1,2,2,3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.remove_duplicates(nums))
