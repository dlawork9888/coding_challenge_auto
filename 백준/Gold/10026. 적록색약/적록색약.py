# 통합
    
from collections import deque

# 입력 처리
N = int(input())
grid = []
for _ in range(N):
    grid.append([x for x in input()])

def bfs(grid):
    # directions
    d_row = [1,0,-1,0]
    d_col = [0,1,0,-1]
    
    count = 0
    visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]
    flag = False
    while True:
        # 시작 노드 찾기
        start_node = [-1,-1]
        break_flag = False
        for row_idx, row in enumerate(visited):
            for col_idx, ele in enumerate(row):
                if ele == False:
                    start_node = [row_idx, col_idx]
                    break_flag = True
                    break
            if break_flag:
                break
        if start_node == [-1,-1]:
            break
        # 시작 노드부터 탐색
        target_color = grid[start_node[0]][start_node[1]]
        dq = deque()
        dq.append(start_node)
        visited[start_node[0]][start_node[1]] = True
        while dq:
            now_row, now_col = dq.popleft()
            for i in range(4):
                next_row = now_row + d_row[i]
                next_col = now_col + d_col[i]
                # in grid + visited?
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and visited[next_row][next_col] == False:
                    # same color?
                    if grid[next_row][next_col] == target_color:
                        dq.append([next_row, next_col])
                        visited[next_row][next_col] = True
        count += 1
    return count

abnormal_grid = [['X' if ele == 'R' or ele == 'G' else 'Y' for ele in row] for row in grid]
print(f"{bfs(grid)} {bfs(abnormal_grid)}")
