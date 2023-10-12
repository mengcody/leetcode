"""
90度旋转
"""


class Solution:
    def rotate(self, matrix):
        # 先转置矩阵
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                print(matrix[i][j])
                # 斜线为轴旋转
                # 1   2   3
                #   \
                # 4   5   6
                #       \
                # 7   8   9
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)
        # 反转每一行
        for i in range(n):
            matrix[i] = matrix[i][::-1]


if __name__ == '__main__':
    solution = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(matrix)
    print(matrix)
