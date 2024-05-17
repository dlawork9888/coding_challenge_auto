from collections import deque
def solution(game_map):
    d_row = [0,1,0,-1]
    d_col = [1,0,-1,0]
    q = deque()
    q.append((0,0))
    while q:
        now_row, now_col = q.popleft()
        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            if 0 <= next_row < len(game_map) and 0 <= next_col < len(game_map[0]):
                if game_map[next_row][next_col] == 1:
                    q.append((next_row, next_col))
                    game_map[next_row][next_col] = game_map[now_row][now_col] + 1
    return -1 if game_map[-1][-1] == 1 or game_map[-1][-1] == 0 else game_map[-1][-1]

#visited 배열 없이 푸는 법
