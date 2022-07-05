class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m = len(heights)
        n = len(heights[0])
        
        to_pacific = set()
        to_atlantic = set()
        
        direction_x = [-1, 1, 0, 0]
        direction_y = [0, 0, -1, 1]
        
        def dfs(i, j, can_reach):
            can_reach.add(tuple([i, j]))
            for k in range(4):
                x = i + direction_x[k]
                y = j + direction_y[k]
                if x >= 0 and x < m and y >= 0 and y < n and heights[x][y] >= heights[i][j] and (x, y) not in can_reach:
                    can_reach.add(tuple([i, j]))
                    dfs(x, y, can_reach)
                
        for i in range(n):
            dfs(0, i, to_pacific)
            dfs(m - 1, i, to_atlantic)
        for i in range(m):
            dfs(i, 0, to_pacific)
            dfs(i, n - 1, to_atlantic)
            
        x = []
        for i in to_pacific:
            if i in to_atlantic:
                x.append(list(i))
        return x
