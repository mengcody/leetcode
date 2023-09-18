class Solution:
    """
    In this solution, we use two pointers, left and right, starting from the ends of the array.
    We also maintain left_max and right_max to keep track of the maximum height encountered from the left and right, respectively.
    We traverse the array, moving the pointers towards each other, and calculate the trapped water at each step.
    The trapped water is the minimum of the maximum heights minus the current height.
    """

    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water


if __name__ == '__main__':
    solution = Solution()
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert 6 == solution.trap(h)
