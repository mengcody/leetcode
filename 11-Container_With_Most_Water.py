class Solution:
    def max_area(self, height: list[int]) -> int:
        # 面积 = 长 * 宽
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            max_area = max(max_area, (right - left) * h)

            # 移动高度较小的，以期望获取更大的面积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert 49 == solution.max_area(height)
