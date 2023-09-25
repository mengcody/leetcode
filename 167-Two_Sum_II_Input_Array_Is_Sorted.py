class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        """
        双指针
        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return None


if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    solution.two_sum(numbers, target)
