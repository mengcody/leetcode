class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        ans = 0
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sas"
    solution.str_str(haystack, needle)
