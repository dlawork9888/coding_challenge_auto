from collections import deque
# 입력 처리
def input_process():
    cols, rows = [int(x) for x in input().split()]
    map = []
    visited = []
    for i in range(rows):
        row = [int(x) for x in input().split()]
        visited_row = []
        for ele in row:
            if ele != -1:
                visited_row.append(False)
            else:
                visited_row.append(True)
        map.append(row)
        visited.append(visited_row)
    return map, visited
    # map => map
    # visted => 방문한 노드(+못가는 노드) => True, 방문 안한 노드 => False, -1이면 방문한 노드 취급
map, visited = input_process()

# 돌아다니면서 1찾기 
dq = deque()
for row_idx, row in enumerate(map):
    for col_idx, ele in enumerate(row):
        if ele == 1:
            dq.append([row_idx, col_idx, 0])
# directions
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]


max_day = 0 
while dq:
    now_node = dq.popleft()
    now_r = now_node[0]
    now_c = now_node[1]
    now_day = now_node[2]
    # 방문 표시
    visited[now_r][now_c] = True
    # max_day 비교
    if max_day < now_day:
        max_day = now_day
    for i in range(4):
        next_r = now_r + d_row[i]
        next_c = now_c + d_col[i]
        next_day = now_day + 1
        # 맵안에 있는지 확인
        if 0 <= next_r < len(map) and 0 <= next_c < len(map[0]):
            # 방문하지 않았고 익힐 수 있는 토마토
            if visited[next_r][next_c] == False and map[next_r][next_c] == 0:
                # 토마토 익히기
                map[next_r][next_c] = 1
                # 덱에 추가
                dq.append([next_r, next_c, next_day])
                
if all([all(row) for row in visited]):
    print(max_day)
else:
    print(-1)