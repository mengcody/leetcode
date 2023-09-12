class Solution:
    """
    remove the duplicate element from a sroted array

    slow-fast pointer

    slow: point to the element need reserver
    fast: traverse the array

    0 0    1 1 1     2 2     3 3 3    4

    slow: point to the right place that the group elment should place 
    fast: traverse the array in one group

    """

    def remove_duplicates(self, nums: list[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                # fast move to the next
                j += 1
            else:
                # slow move to the next element
                i += 1
                # put the j element to i element
                nums[i] = nums[j]
                j += 1

        return i + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().remove_duplicates(nums))
