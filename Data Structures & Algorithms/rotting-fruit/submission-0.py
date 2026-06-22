class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1

        q = collections.deque()
        visit = set()
        for r in range((ROWS)):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        time = 0
        rotten_fruits = 0
        while q and fresh_fruits > rotten_fruits:
            time += 1
            for i in range(len(q)):
                new_r,new_c = q.popleft()
                for a,b in [[0,1],[0,-1],[-1,0],[1,0]]:
                    r = a + new_r
                    c = b + new_c
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visit:
                        pass
                    else:
                        rotten_fruits += 1
                        visit.add((r,c))
                        q.append((r,c))
        return time if fresh_fruits == rotten_fruits else -1