class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1


        