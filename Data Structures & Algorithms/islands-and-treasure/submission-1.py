# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         # if not grid:
#         #     return []


#         ROWS, COLS = len(grid), len(grid[0])
#         # visit = set()
#         directions = [[1,0], [-1,0], [0,1], [0,-1]]
#         INF = 2147483647

#         def bfs(r, c):
#             q = deque([(r,c)])
#             visit = [[False] * COLS for _ in range(ROWS)]
#             visit[r][c] = True
#             # q.append((r,c))
#             steps = 0

#             while q:
#                 for _ in range(len(q)):
#                     row, col = q.popleft()
#                     if grid[row][col] == 0:
#                         return steps
#                     for dr, dc in directions:
#                         nr, nc = row+dr, col+dc
#                         # if ((row,col) in visit or min(col, row) < 0 or rol == ROWS or col == COLS or grid[row][col] == -1):
#                         #     continue
#                         if (0 <= nr < ROWS and 0 <=nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1):
#                             visit[nr][nc] = True
#                         # if grid[row][col] == 0:
#                         #     count += 1
#                             q.append((nr, nc))
#                         # visit.add(row, col)
#                 steps += 1
#             return INF

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == INF:
#                     grid[r][c] = bfs(r,c)


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()
        visit = [[False] * COLS for _ in range(ROWS)]

        # 所有宝箱一起作为起点
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit[r][c] = True

        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = steps          # 出队时写入距离
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and not visit[nr][nc] and grid[nr][nc] != -1):
                        visit[nr][nc] = True
                        q.append((nr, nc))
            steps += 1
