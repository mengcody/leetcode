class Solution:
    def is_valid(self, arr):
        seen = set()
        for v in arr:
            if v != ".":
                if v in seen:
                    return False
                seen.add(v)

        return True

    def is_valid_sudoku(self, board):
        for i in range(9):
            # 遍历行, 判断每一行是否ok
            if not self.is_valid(board[i]):
                return False
            # 判断列
            if not self.is_valid([board[j][i] for j in range(9)]):
                return False

        # 判断3 * 3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(sub_grid):
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()
    input = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert solution.is_valid_sudoku(input)
