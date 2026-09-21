class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        max_islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def bfs(r, c):
            count = 0
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                count += 1
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(ROWS) and c in range(COLS) and (r, c) not in visit and grid[r][c] == 1):
                        q.append((r,c))
                        visit.add((r,c))
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_islands = max(max_islands, bfs(r, c))

        return max_islands
            