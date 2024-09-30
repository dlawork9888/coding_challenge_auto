# 통합

# 입력처리
N, M = [int(x) for x in input().split()]
grid = []
for _ in range(N):
    grid.append([int(x) for x in input()])
    
    
from collections import deque

# directions
d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

queue = deque()
# BFS
queue.append([0,0])
while queue:
    now_node = queue.popleft()
    for i in range(4):
        next_row = now_node[0] + d_row[i]
        next_col = now_node[1] + d_col[i]
        # in grid ? and able to go?
        if (0<=next_row<N and 0<=next_col<M) and (grid[next_row][next_col] == 1):
            grid[next_row][next_col] = grid[now_node[0]][now_node[1]] + 1
            queue.append([next_row, next_col])
print(grid[-1][-1])