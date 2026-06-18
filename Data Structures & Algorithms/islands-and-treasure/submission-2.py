class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
    
        while q:
            curr_r,curr_c = q.popleft()
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                curr_dr = curr_r+dr
                curr_dc = curr_c+dc
                
                if curr_dr < 0 or curr_dc < 0 or curr_dr >= rows or curr_dc >= cols or grid[curr_dr][curr_dc] != 2147483647:
                    pass
                else:
                    grid[curr_dr][curr_dc] = grid[curr_r][curr_c] + 1
                    q.append((curr_dr, curr_dc))