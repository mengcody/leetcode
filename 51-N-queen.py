"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
"""


class Solution:
    def solve_n_queens(self, n: int) -> list[list[str]]:
        def is_valid(board, row, col, n):
            # 检查同一列是否有皇后
            for i in range(row):
                if board[i][col] == 1:
                    return False

            # 检查左上方是否有皇后
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            # 检查右上方是否有皇后
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            if row == n:
                # 将当前解加入结果
                result.append([''.join(['Q' if col == 1 else '.' for col in row]) for row in board])
                return

            for col in range(n):
                if is_valid(board, row, col, n):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

        result = []
        board = [[0] * n for _ in range(n)]
        backtrack(0)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.solve_n_queens(4)
    for r in result:
        for x in r:
            print("    ".join([c for c in x]))
        print("=================")
