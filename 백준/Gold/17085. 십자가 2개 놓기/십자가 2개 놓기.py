# 입력 처리
n_row, n_col = [int(x) for x in input().split()]

grid = []
for i in range(n_row):
    grid.append([True if x == '#' else False for x in input()])

# 십자가 최대 길이
max_length = min(n_col, n_row) if min(n_col, n_row) % 2 == 1 else min(n_col, n_row) - 1

from collections import defaultdict


# center_loc => [center_row, center_col]
# shift => center를 기준으로 몇칸을 이동하는지
def center_validation(grid, center_loc, shift):
    #print(f'center_loc: {center_loc}')
    #print(f'shift: {shift}')
    center_row, center_col = center_loc
    ##### 중심은 못가는 위치인가?
    if grid[center_row][center_col] == False:
        return False
    ##### 아래로
    for i in range(1, shift + 1):
        # 그리드 안쪽에 없나? 못가는 위치인가? => 하나라도 걸리면 return False
        if 0 <= center_row + i < len(grid) and 0 <= center_col < len(grid[0]) and grid[center_row + i][center_col] == True:
            pass
        else:
            return False
    ##### 위로
    for i in range(1, shift + 1):
        # 그리드 안쪽에 없나? 못가는 위치인가? => 하나라도 걸리면 return False
        if 0 <= center_row - i < len(grid) and 0 <= center_col < len(grid[0]) and grid[center_row - i][center_col] == True:
            pass
        else:
            return False
    ##### 오른쪽으로
    for i in range(1, shift+1):
        # 그리드 안쪽에 없나? 못가는 위치인가? => 하나라도 걸리면 return False
        if 0 <= center_row < len(grid) and 0 <= center_col + i < len(grid[0]) and grid[center_row][center_col + i] == True:
            pass
        else:    
            return False
    ##### 왼쪽으로
    for i in range(1, shift+1):
        # 그리드 안쪽에 없나? 못가는 위치인가? => 하나라도 걸리면 return False
        if 0 <= center_row < len(grid) and 0 <= center_col - i < len(grid[0]) and grid[center_row][center_col - i] == True:
            pass
        else:    
            return False
    return True

center_locs = defaultdict(list)

for cross_length in range(max_length, 0, -2): # 5,3,1
    #print(f'cross_length: {cross_length}')
    # 몇번째 row
    for row in range(cross_length//2, n_row - cross_length//2):
        for col in range(cross_length//2, n_col - cross_length//2):
            if center_validation(grid, [row, col], cross_length//2) == True:
                center_locs[cross_length].append([row,col])

def return_combs(center_locs):
    keys = list(center_locs.keys())
    #print(keys)
    combs = []
    for first_idx ,first_key in enumerate(keys):
        for second_idx, second_key in enumerate(keys[first_idx:]):
            if len(center_locs[second_key]) == 1:
                continue
            combs.append((first_key, second_key))
    combs.sort(key = lambda x: -((x[0]*2-1)*(x[1]*2-1)))
    return combs

import copy

def draw_on_grid(temp_grid, center_loc, shift):
    center_row, center_col = center_loc
    ##### 아래로
    for i in range(1, shift+1):
        temp_grid[center_row + i][center_col] = False
    ##### 위로
    for i in range(1, shift+1):
        temp_grid[center_row - i][center_col] = False
    ##### 오른쪽
    for i in range(1, shift+1):
        temp_grid[center_row][center_col + i] = False
    ##### 왼쪽
    for i in range(1, shift+1):
        temp_grid[center_row][center_col - i] = False
    return temp_grid 


def last_step(grid, center_locs):
    for comb in return_combs(center_locs):
        if comb[0] == comb[1]: # 길이가 같은 조합에 대해
            cross_length = comb[0]
            locs = center_locs[cross_length]
            for first_idx, first_loc in enumerate(locs):
                temp_grid = copy.deepcopy(grid)
                temp_grid = draw_on_grid(temp_grid, first_loc, cross_length//2)
                for second_loc in locs[first_idx + 1:]:
                    if center_validation(temp_grid, second_loc, cross_length//2) == True:
                        return (cross_length*2-1)**2
        else: #길이가 다른 조합에 대해
            first_locs = center_locs[comb[0]]
            second_locs = center_locs[comb[1]]
            for first_loc in first_locs:
                temp_grid = copy.deepcopy(grid)
                temp_grid = draw_on_grid(temp_grid, first_loc, comb[0]//2)
                #print(temp_grid)
                for second_loc in second_locs:
                    if center_validation(temp_grid, second_loc, comb[1]//2) == True:
                        return (comb[0]*2-1)*(comb[1]*2-1)

print(last_step(grid, center_locs))