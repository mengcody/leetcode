class Solution:
    """
    快慢指针：快指针找不相同的元素，慢指针指在相等的元素位置, 快指针找到不等于value的值的时候, 将这个值放在相等的这个位置上

    [0,    1,     2,      2,      3,      0,      4,      2]

     ^            ^               ^
     |            |               |
     |            i               j

    i,j

    开始的时候，一起走，
    遇到与给定的元素相同的元素的时候, i就不走了, j继续走, j 走到不等的地方的时候, 将这个地方的值放到i的位置处

    """

    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            elif nums[j] == val:
                j += 1

        print(nums)
        return i


if __name__ == "__main__":
    solution = Solution()
    nums = [2]
    val = 3
    k = solution.removeElement(nums, val)
    print(k)
