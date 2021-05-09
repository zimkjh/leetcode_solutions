class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        answer = 0
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        def bfs(x, y):
            queue = [(x, y)]
            visited[x][y] = True
            while queue:
                print(x, y, queue)
                now = queue.pop(0)
                for i in range(4):
                    newX = now[0] + dx[i]
                    newY = now[1] + dy[i]
                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]) or visited[newX][newY]:
                        continue
                    if grid[newX][newY] == "1": 
                        queue.append((newX,newY))
                        visited[newX][newY] = True
                    else:
                        visited[newX][newY] = True
                
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] :
                    continue
                if grid[i][j]== "1":
                    bfs(i, j)
                    answer += 1
        return answer
            
        