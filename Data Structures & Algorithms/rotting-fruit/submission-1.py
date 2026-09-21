class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visit.add((row, col))
                elif grid[row][col] == 1:
                    fresh += 1


        def addFruit(r, c):
            nonlocal fresh
            if (r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c] == 0):
                return
            visit.add((r,c))
            q.append((r,c))
            fresh -= 1


        steps = 0
        while q and fresh >0:
            for _ in range(len(q)):
                r, c = q.popleft()
                addFruit(r+1, c)
                addFruit(r-1,c)
                addFruit(r,c+1)
                addFruit(r,c-1)

            steps+=1
        return steps if fresh == 0 else -1