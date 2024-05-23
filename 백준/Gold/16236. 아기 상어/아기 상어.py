##### 수정 => 일단 다 탐색하고 먹을 수 있는 애들 좌표를 모으고 정렬

N = int(input())
grid = []
for _ in range(N):
    row = [int(x) for x in input().split()]
    grid.append(row)

# 전역 변수 => 상어 크기, 먹은 물고기 수
shark_size = 2
eat_count = 0
# grid는 어차피 리스트 => 전역으로 사용, 포인터 전달
### 상어 위치 찾기
def search_shark_loc(N, grid): 
    shark_loc = [-1,-1]
    for row_idx, row in enumerate(grid):
        for col_idx, ele in enumerate(row):
            if ele == 9:
                shark_loc[0] = row_idx
                shark_loc[1] = col_idx
    return shark_loc
    # [-1,-1]이면 못찾은거

# test
#print(f'shark_loc: {search_shark_loc(test_N, test_grid)}')


### 상어 위치에서 제일 가까운 먹을 수 있는 물고기 찾기

# directions(전역으로 사용) => 상좌우하
d_row = [-1,0,0,1] # 위쪽은 -1 !!!!
d_col = [0,-1,1,0]

from collections import deque

def search_nearest_fish(N, grid, shark_loc):
    # 전역으로 사용할거면 그냥 리스트로 해버릴 걸... 으아
    global shark_size 
    global eat_count 
    edibles = []
    #print(f'shark_size: {shark_size }')
    visited = [[False for ele in range(N)] for row in range(N)]
    q = deque()
    q.append([shark_loc[0], shark_loc[1], 0]) # row, col, count
    visited[shark_loc[0]][shark_loc[1]] = True
    while q:
        # unpack
        now_row, now_col, now_time_taken = [x for x in q.popleft()]
        #print(f'------now_node: {now_row, now_col}')
        for i in range(4):
            next_row = now_row + d_row[i]
            next_col = now_col + d_col[i]
            # 그리드 안쪽 + 미방문 체크
            if 0 <= next_row < N and 0 <= next_col < N and visited[next_row][next_col] == False:
                # 그 위치가 갈 수 있는 곳인가?
                #print(f'갈 수 있음! {[next_row, next_col]}')
                if grid[next_row][next_col] <= shark_size:
                    # 혹시 먹을 수도 있나?
                    if 0 < grid[next_row][next_col] < shark_size:
                        #print(f'먹을 수 있음! {[next_row, next_col]}')
                        # edibles 에 추가
                        edibles.append([next_row, next_col, now_time_taken + 1])
                    # 먹을 수 없는 자리
                    q.append([next_row, next_col, now_time_taken + 1])
                    visited[next_row][next_col] = True
    edibles.sort(key = lambda x: (x[2], x[0], x[1])) # 거리, 행, 열
    if edibles:
        move_row, move_col, move_time = edibles[0]
        # 이동
        grid[move_row][move_col] = 9
        grid[shark_loc[0]][shark_loc[1]] = 0
        # 체급 키우기
        eat_count += 1
        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0
        return move_time
    else:
        return False
full_time_taken = 0
while True:
    shark_loc = search_shark_loc(N, grid)
    time_taken = search_nearest_fish(N, grid, shark_loc)
    if time_taken != False:
        full_time_taken += time_taken
    else: 
        break
print(full_time_taken)
