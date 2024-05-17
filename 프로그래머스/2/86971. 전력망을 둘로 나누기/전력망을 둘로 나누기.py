from itertools import combinations
from collections import deque
import copy
import math 

def return_adj_mat(n,wires):
    adj_mat = [[False for x in range(n)] for x in range(n)]
    
    for wire in wires:
        adj_mat[wire[0]-1][wire[1]-1] = True
        adj_mat[wire[1]-1][wire[0]-1] = True
    
    return adj_mat


def return_after(n, input_adj_mat):
    adj_mat = copy.deepcopy(input_adj_mat)
    queue = deque()
    
    #시작 노드
    start_node = -1
    for i in range(n):
        for j in range(n):
            if adj_mat[i][j] == True:
                start_node = i

    queue.append(start_node)
    count = 1
    while queue:
        now_node = queue.pop()
        for i in range(n):
            if adj_mat[now_node][i] == True:
                queue.append(i)
                count += 1
                adj_mat[now_node][i] = False
                adj_mat[i][now_node] = False
    
    return count, adj_mat


def solution(n, wires):
    coms = combinations(wires, n-2)
    min_count = math.inf 
    for com in coms:
        com = list(com)
        input_adj_mat = return_adj_mat(n, com)
        count_1, input_adj_mat = return_after(n, input_adj_mat)
        count_2, input_adj_mat = return_after(n, input_adj_mat)
        if min_count > abs(count_1 - count_2):
            min_count = abs(count_1 - count_2)
    return min_count
