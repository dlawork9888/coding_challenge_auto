# 통합

# 입력처리
# 정점수 간선수 시작정점
N, M, R = [int(x) for x in input().split()]
# 인접 리스트
from collections import defaultdict
adj_list = defaultdict(list)
for _ in range(M):
    u, v = [int(x) for x in input().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)
    
# 오름차순으로 방문 -> 큰거 거 먼저 스택에 들어감
for key in adj_list.keys():
    adj_list[key].sort()

import sys
sys.setrecursionlimit(150000)
    
# DFS
visited = [0 for _ in range(N+1)]
count = [1]

def dfs(now_node):
    visited[now_node] = count[0]
    count[0] += 1
    for adj_node in adj_list[now_node]:
        if visited[adj_node] == 0:
            dfs(adj_node)
            
dfs(R)

for order in visited[1:]:
    print(order)