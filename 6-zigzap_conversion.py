class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or len(s) <= num_rows:
            return s

        rows = ['' for _ in range(num_rows)]

        row_idx = 0  # 应该放在第几行
        direction = 1  # 1: down, -1: up

        for c in s:
            rows[row_idx] += c

            if row_idx == 0:  #  如果是0行，此时应该向下走了
                direction = 1
            elif row_idx == num_rows - 1:  # 如果到了最后一行，应该向上走了
                direction = -1

            row_idx += direction   # 此时的行号应该是 当前的行号 + 方向

        return ''.join(rows)


if __name__ == '__main__':
    solution = Solution()
    assert "PAHNAPLSIIGYIR" == solution.convert("PAYPALISHIRING", 3)
