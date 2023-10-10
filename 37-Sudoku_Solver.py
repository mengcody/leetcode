class Solution:
    def solve_sudoku(self, board):
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[row // 3 * 3 + i // 3][
                    col // 3 * 3 + i % 3] == num:
                    return False
            return True

        # 找到就返回
        def backtrack():
            # 一行一行的填数
            for i in range(9):
                for j in range(9):
                    # 遍历到 . 的时候，需要进行处理
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            # 判断这个num，放在这里合适不
                            if is_valid(i, j, num):
                                # 选择
                                board[i][j] = num
                                # 递归, 找到合适的就返回
                                if backtrack():
                                    return True
                                # 回溯
                                board[i][j] = '.'
                        return False
            return True

        backtrack()


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution.solve_sudoku(board)
    for i in range(len(board)):
        print(board[i])
