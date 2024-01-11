# 통합
# 입력처리
map = []
for i in range(int(input())):
    row = [int(x) for x in input()]
    map.append(row)

from collections import deque

how_many_danjis = 0
count = []
# directions
d_row = [1,0,-1,0]
d_col = [0,1,0,-1]
while any([any(row) for row in map]): # map에서 어느 하나라도 1이라면 계속 실행
    # 최초의 1찾기
    one_loc = [-1,-1]
    flag = True
    for row_idx, row in enumerate(map):
        for col_idx, ele in enumerate(row):
            if ele == 1:
                one_loc = [row_idx, col_idx]
                flag = False
                break
        if flag == False:
            break
    # map에 더이상 1이 없다!? => 그만
    if one_loc[0] == -1 and one_loc[1] == -1:
        break
    # dfs
    now_count = 0 # 붙어있는 집이 몇 개?
    dq = deque()
    dq.append(one_loc)
    # 방문 표시
    map[one_loc[0]][one_loc[1]] = 0
    while dq:
        now_node = dq.pop()
        #print(f'now_node : {now_node}')
        # 노드 분해
        now_r = now_node[0]
        now_c = now_node[1]
        # now_count += 1
        now_count += 1
        # 주변 노드 탐색
        for i in range(4):
            next_r = now_r + d_row[i]
            next_c = now_c + d_col[i]
            # map 범위 안에 있나?
            if 0 <= next_r < len(map) and 0 <= next_c < len(map[0]):
                # 탐색이 가능한 노드인가? (방문할 수 있는가?)
                if map[next_r][next_c] == 1:
                    # 맞다면 dq에 추가하자
                    dq.append([next_r, next_c])
                    # 방문 표시
                    map[next_r][next_c] = 0
    # 탐색이 끝났으면 => now_count 를 count 에 추가, how_many_danjis += 1
    #print(f'탐색 끝!')
    count.append(now_count)
    how_many_danjis += 1

print(how_many_danjis)
count.sort()
for c in count:
    print(c)
            