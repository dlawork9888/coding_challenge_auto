from collections import deque

N = int(input())
map = [-1 for _ in range(N)]
count = 0

col_check = [False for _ in range(N)]
up_diag_check = [False for _ in range(2*N-1)] 
down_diag_check = [False for _ in range(2*N-1)]

def is_valid(row_num, col_num):
    return not (col_check[col_num] or up_diag_check[row_num + col_num] or down_diag_check[row_num - col_num + N - 1])

def dfs(n):
    global count
    if n == N:
        count += 1
    else:
        for i in range(N):
            if is_valid(n, i):
                map[n] = i
                col_check[i] = True
                up_diag_check[n + i] = True
                down_diag_check[n - i + N - 1] = True
                dfs(n + 1)
                col_check[i] = False
                up_diag_check[n + i] = False
                down_diag_check[n - i + N - 1] = False

dfs(0)
print(count)
