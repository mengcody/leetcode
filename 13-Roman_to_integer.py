class Solution:
    """
    We iterate through the Roman numeral string, comparing the current value to the previous value.
    If the current value is greater than the previous value,
    we subtract twice the previous value from the total (following the Roman numeral subtraction rules),
    otherwise, we add the current value to the total.
    """

    def roman_to_int(self, s: str) -> int:
        roman_to_int_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for ch in s:
            curr_value = roman_to_int_mapping[ch]
            if curr_value > prev_value:
                # we need to subtract twice the previous value
                # because we've already added the previous value in the previous iteration.
                total += curr_value - prev_value - prev_value  # 这里是关键, 减去加过的一次, 当前的值需要用后面的减去前面的
            else:
                total += curr_value
            prev_value = curr_value

        return total


if __name__ == '__main__':
    solution = Solution()
    s = "III"
    assert 3 == solution.roman_to_int(s)
