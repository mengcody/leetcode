class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """solution1
        暴力破解：
        """
        new_nums = []
        for i in range(len(nums)):
            new_nums.append(self._product_array(nums[:i] + nums[i + 1 :]))

        return new_nums

    def _product_array(self, nums: list[int]) -> int:
        product = 1
        print(nums)
        for n in nums:
            product *= n
            print(product)
        return product

    """
    solution2:
    * calculate the left
    * calculate the right
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

    """


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.product_except_self(nums))
