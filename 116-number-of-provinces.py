class Solution:
    def find_circle_num(self, is_connected: list[list[int]]) -> int:

        def dfs(i):
            visited.add(i)
            for j in range(len(is_connected)):
                if is_connected[i][j] == 1 and j not in visited:
                    dfs(j)

        provinces = 0
        visited = set()
        for i in range(len(is_connected)):
            if i not in visited:
                provinces += 1
                dfs(i)  # 每次完成DFS遍历后，所有标记为已访问的节点构成一个连通分量
        return provinces
