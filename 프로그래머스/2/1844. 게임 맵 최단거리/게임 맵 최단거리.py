from collections import deque as dq

def solution(maps):
    d_row = [0,1,0,-1]
    d_col = [1,0,-1,0]
    # BFS
    q = dq()
    start_node = [0,0]
    q.append(start_node)
    while q:
        now_row, now_col = q.popleft()
        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            # in maps ? is able to go ?
            if 0 <= next_row < len(maps) and 0 <= next_col < len(maps[0]) and maps[next_row][next_col] == 1:
                maps[next_row][next_col] = maps[now_row][now_col] + 1 
                q.append([next_row, next_col])
    return -1 if maps[-1][-1] == 1 else maps[-1][-1]