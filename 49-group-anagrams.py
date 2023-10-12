from collections import defaultdict


class Solution:
    def group_anagrams(self, strs):
        anagram_groups = defaultdict(list)
        # 排序后的word作为key
        for word in strs:
            sorted_word = "".join(sorted(word))
            print(sorted_word)
            anagram_groups[sorted_word].append(word)
            print(anagram_groups)

        result = [group for group in anagram_groups.values()]
        return result


if __name__ == '__main__':
    solution = Solution()
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.group_anagrams(s))


    def find_min(nums):
        min_v = float('inf')
        for num in nums:
            if num < min_v:
                min_v = num
        return min_v


    def find_max():
        arr = [3, 7, 4, 6, 1, 2, 5]
        result = float('-inf')
        for i in range(len(arr)):
            result = max(result, arr[i] // find_min(arr[i:]))
        return result


    print(find_max())


    def max_ratio(arr):
        if not arr or len(arr) < 2:
            return None

        min_value = float('inf')  # 记录最小值
        max_ratio = float('-inf')  # 记录最大比值

        for num in arr:
            if num < min_value:
                min_value = num
            else:
                max_ratio = max(max_ratio, num / min_value)

        return max_ratio


    print(max_ratio([3, 7, 4, 6, 1, 2, 5]))

    nums = [1, 2, 3, 4, 5, 7, 8, 6, 9]
    # 从nums中等概率的取m个不同的数
    # 1. 随机取一个, 然后将这个剔除  1/n
    # 2. 在随机取一个 1/(n -1)
