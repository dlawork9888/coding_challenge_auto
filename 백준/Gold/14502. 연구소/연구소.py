# 끊겨서 다시 풀기
import copy

### 입력 처리
N, M = [int(x) for x in input().split()]
lab_map = []
for _ in range(N):
    lab_map.append([int(x) for x in input().split()])

    
##### 디버그 용도 테스트 입력
"""
N,M = 7,7
lab_map = [
    [2,0,0,0,1,1,0],
    [0,0,1,0,1,2,0],
    [0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0]
]
"""
### 퍼져나갔을 때 안전 영역의 크기를 반환하는 함수
# directions
d_row = [0,1,0,-1]
d_col = [1,0,-1,0]
def how_many_zeros_after_diffusion(lab_map):
    # 확산
    while True:
        # 시작 노드 찾기
        start_node = [-1,-1]
        for row_idx, row in enumerate(lab_map):
            for col_idx, ele in enumerate(row):
                if ele == 2:
                    start_node[0] = row_idx
                    start_node[1] = col_idx
        if start_node[0] == -1 and start_node[1] == -1:
            break
        # diffusion start
        # 확산된 건 3으로
        lab_map[start_node[0]][start_node[1]] = 3
        stack = []
        stack.append(start_node) 
        while stack:
            now_row, now_col = stack.pop()
            for i in range(4):
                next_row = now_row + d_row[i]
                next_col = now_col + d_col[i]
                # in map?
                if 0 <= next_row < len(lab_map) and 0 <= next_col < len(lab_map[0]):
                    # able to diffusion?
                    if lab_map[next_row][next_col] == 0:
                        lab_map[next_row][next_col] = 3
                        stack.append([next_row, next_col])
    # 확산 후 0 count
    count = 0
    for row in lab_map:
        for ele in row:
            if ele == 0:
                count += 1
    """
    # debug
    if count > 30:
        print(count)
    
        # debug
        for row in lab_map:
            for ele in row:
                print(ele, end = ' ')
            print()
        print()
        print()
    """
    return count

### 벽 세우기
# 모든 0의 좌표
zero_locs = []
for row_idx, row in enumerate(lab_map):
    for col_idx, ele in enumerate(row):
        if ele == 0:
            zero_locs.append([row_idx, col_idx])
# 벽 3개 세우기
max_count = -1
for first_loc_idx, first_loc in enumerate(zero_locs[:-2]):
    for second_loc_idx, second_loc in enumerate(zero_locs[first_loc_idx + 1:-1]):
        second_loc_idx += first_loc_idx + 1
        for third_loc_idx, third_loc in enumerate(zero_locs[second_loc_idx + 1:]):
            test_lab_map = copy.deepcopy(lab_map)
            test_lab_map[first_loc[0]][first_loc[1]] = 1
            test_lab_map[second_loc[0]][second_loc[1]] = 1
            test_lab_map[third_loc[0]][third_loc[1]] = 1
            now_count = how_many_zeros_after_diffusion(test_lab_map)
            if now_count > max_count:
                max_count = now_count
print(max_count)