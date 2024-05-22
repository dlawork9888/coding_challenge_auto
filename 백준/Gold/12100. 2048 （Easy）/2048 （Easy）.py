## 입력 처리

def input_process():
    N = int(input())
    grid = []
    for i in range(N):
        grid.append([int(x) for x in input().split()])
    return N, grid

N, input_grid = input_process()
# col의 첫 원소부터 순회
# 0이 아닌 원소를 저장
# 저장배열을 순회하며 재배치
# 저장 배열에 [4,2,2]
# 덱을 이용
from collections import deque
import copy

test_N = 6
test_grid = [
    [2,2,0,0,0,0],
    [0,0,2,0,2,0],
    [0,0,0,2,2,0],
    [0,0,4,0,0,0],
    [0,0,4,0,4,0],
    [0,0,0,0,0,0]
]

def up(N, grid):
    for col_idx in range(N):
        # 0이 아닌 원소를 not_zero_dq에 push
        not_zero_dq = deque()
        for row_idx in range(N):
            if grid[row_idx][col_idx] != 0:
                not_zero_dq.append(grid[row_idx][col_idx])
        # 합쳐지는게 있다면 합치고 allocate리스트에 push
        # 덱이 차있는 동안, 
        # 빼고, 뺀게 [0]이랑 같다면 또 뺴고 합쳐서 넣기
        # 아니라면 그냥 넣기
        allocate = []
        while not_zero_dq:
            now_ele = not_zero_dq.popleft()
            if not_zero_dq and not_zero_dq[0] == now_ele:
                now_ele += not_zero_dq.popleft()
                allocate.append(now_ele)
                continue
            allocate.append(now_ele)
        # 배치
        # allocate 리스트에 있는 애들을 위에서 부터 박고
        for row_idx in range(len(allocate)):
            grid[row_idx][col_idx] = allocate[row_idx]
        # 나머지 애들은 0으로 채우가
        for row_idx in range(len(allocate), N):
            grid[row_idx][col_idx] = 0
        ### 해당 열 종료
    return grid
    
#up(6, test_grid)

def down(N, grid):
    for col_idx in range(N):
        # 0이 아닌 원소를 not_zero_dq에 push, 아래에서 위로 순회하면서
        not_zero_dq = deque()
        for row_idx in range(N-1,-1,-1):
            if grid[row_idx][col_idx] != 0:
                not_zero_dq.append(grid[row_idx][col_idx])
        # 합쳐지는게 있다면 합치고 allocate리스트에 push
        #print(f'not_zero_dq: {not_zero_dq}')
        allocate = []
        while not_zero_dq:
            now_ele = not_zero_dq.popleft()
            if not_zero_dq and not_zero_dq[0] == now_ele:
                now_ele += not_zero_dq.popleft()
                allocate.append(now_ele)
                continue
            allocate.append(now_ele)
        #print(f'allocate: {allocate}')
        # 배치
        for idx, row_idx in enumerate(range(N-1, N-1-len(allocate), -1)):
            #print(row_idx)
            grid[row_idx][col_idx] = allocate[idx]
        for row_idx in range(N-1-len(allocate), -1, -1):
            grid[row_idx][col_idx] = 0
        ### 해당 열 종료
    return grid
    
#down(6, test_grid)

def left(N, grid):
    for row_idx in range(N):
    # 0이 아닌 원소를 not_zero_dq에 push, 왼쪽에서 오른쪽으로 순회하면서
        not_zero_dq = deque()
        for col_idx in range(N):
            if grid[row_idx][col_idx] != 0:
                not_zero_dq.append(grid[row_idx][col_idx])
        #print(f'not_zero_dq: {not_zero_dq}')
        # 합쳐지는게 있다면 합치고 allocate리스트에 push
        #print(f'not_zero_dq: {not_zero_dq}')
        allocate = []
        while not_zero_dq:
            now_ele = not_zero_dq.popleft()
            if not_zero_dq and not_zero_dq[0] == now_ele:
                now_ele += not_zero_dq.popleft()
                allocate.append(now_ele)
                continue
            allocate.append(now_ele)
        #print(f'allocate: {allocate}')
        # 배치
        for col_idx in range(len(allocate)):
            grid[row_idx][col_idx] = allocate[col_idx]
        for col_idx in range(len(allocate), N):
            grid[row_idx][col_idx] = 0
        ### 해당 행 종료
    return grid
      
#left(6, test_grid)

def right(N, grid):
    for row_idx in range(N):
    # 0이 아닌 원소를 not_zero_dq에 push, 오른쪽에서 왼쪽으로 순회하면서
        not_zero_dq = deque()
        for col_idx in range(N-1, -1, -1):
            if grid[row_idx][col_idx] != 0:
                not_zero_dq.append(grid[row_idx][col_idx])
        #print(f'not_zero_dq: {not_zero_dq}')
        # 합쳐지는게 있다면 합치고 allocate리스트에 push
        #print(f'not_zero_dq: {not_zero_dq}')
        allocate = []
        while not_zero_dq:
            now_ele = not_zero_dq.popleft()
            if not_zero_dq and not_zero_dq[0] == now_ele:
                now_ele += not_zero_dq.popleft()
                allocate.append(now_ele)
                continue
            allocate.append(now_ele)
        #print(f'allocate: {allocate}')
        for idx, col_idx in enumerate(range(N-1, N-len(allocate)-1, -1)):
            grid[row_idx][col_idx] = allocate[idx]
        for col_idx in range(N-len(allocate)-1,-1,-1):
            grid[row_idx][col_idx] = 0
        ### 해당 행 종료
    return grid
        
#right(6, test_grid)  

def calculate_max_value(grid):
    max_value = 0
    for row in grid:
        for ele in row:
            if ele > max_value:
                max_value = ele
    return max_value

##### dfs
func_list = [up, down, left, right]
start_node = [input_grid, 0, calculate_max_value(input_grid)]
stack = []
stack.append(start_node)
max_value = 0
while stack:
    now_grid, now_move_time, now_max_value = stack.pop()
    if now_move_time == 5:
        continue
    # 상 하 좌 우 이동
    for i in range(4):
        before_grid = copy.deepcopy(now_grid)
        after_grid = func_list[i](N, before_grid)
        after_max_value = calculate_max_value(after_grid)
        if max_value < after_max_value:
            max_value = after_max_value
        stack.append([after_grid, now_move_time + 1, after_max_value])

print(max_value)