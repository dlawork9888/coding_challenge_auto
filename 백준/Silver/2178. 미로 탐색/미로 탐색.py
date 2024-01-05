import math

rows, cols = [int(x) for x in input().split()] 
map = []
for _ in range(rows):
    row = []
    for x in input():
        if x == '1':
            row.append(True) # 갈 수 있음
        else:
            row.append(False) # 갈 수 없음
    map.append(row)
path_len_map = [[math.inf for _ in range(cols)] for _ in range(rows)]

from collections import deque

# directions
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]

start_node = [0,0]
dq = deque()
dq.append(start_node)

path_len_map[0][0] = 1
while dq:
    # 노드 까기
    # 방문 표시
    # 주변 노드 탐색
    # 주변 갈 수 있는 노드에 지금 노드의 path len + 1
    now_node = dq.popleft()
    #print(f'now_node : {now_node}')
    now_r = now_node[0]
    now_c = now_node[1]
    map[now_r][now_c] = False
    now_path_len = path_len_map[now_r][now_c]
    for i in range(4):
        next_node = [now_r + d_row[i], now_c + d_col[i]]
        #print(f'next_node : {next_node}')
        next_r = next_node[0]
        next_c = next_node[1]
        # in map? 
        if 0 <= next_r < len(map) and 0 <= next_c < len(map[0]):
            #print(f'in map!')
            # not visited?
            if map[next_r][next_c] == True: # 갈 수 있으면
                #print(f'now visited!')
                # 원래 path len보다 짧으면
                if path_len_map[next_r][next_c] > now_path_len + 1:
                    path_len_map[next_r][next_c] = now_path_len + 1 # 갱신
                    dq.append(next_node)
print(path_len_map[-1][-1])