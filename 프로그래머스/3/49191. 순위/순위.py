from collections import defaultdict
from collections import Counter

### FOR DEBUGGING
def print_mat(mat):
    for row in mat:
        for ele in row:
            print(ele, end = '  ')
        print()
        
def solution(n, results):
    # 플로이드 와샬 => 인접 행렬
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for result in results:
        adj_mat[result[0]-1][result[1]-1] = 1 
        adj_mat[result[1]-1][result[0]-1] = 2
        
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if adj_mat[start][mid] == 1 and adj_mat[mid][end] == 1:
                    adj_mat[start][end] = 1
                    adj_mat[end][start] = 2
    #print_mat(adj_mat)
    count = 0
    for row in adj_mat:
        if Counter(row)[0] == 1:
            count += 1
    
    return count
    