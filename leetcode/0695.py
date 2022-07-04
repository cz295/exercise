class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        visited = set([])
        max_area = 0

        def check_island(i, j):
            nonlocal max_area
            nonlocal area
            if grid[i][j] == 1 and (i, j) not in visited:
                area += 1
                visited.add(tuple([i, j]))
                if area > max_area:
                    max_area = area
                if i < m - 1:
                    check_island(i + 1, j)
                if j < n - 1:
                    check_island(i, j + 1)
                if i > 0:
                    check_island(i - 1, j)
                if j > 0:
                    check_island(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = 0
                    check_island(i, j)
        return max_area
