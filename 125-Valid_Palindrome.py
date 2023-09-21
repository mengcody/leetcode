class Solution:
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            print(s[left].lower(), s[right].lower())
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    assert True is solution.is_palindrome(s)
