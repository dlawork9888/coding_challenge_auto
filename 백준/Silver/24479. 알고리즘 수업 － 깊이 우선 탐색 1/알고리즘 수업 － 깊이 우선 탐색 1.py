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
    
for key in adj_list.keys():
    adj_list[key].sort(reverse = True)
    
    
visited = [0 for _ in range(N+1)]

stack = []
stack.append(R)

count = 1
while stack:
    now_node = stack.pop()
    if visited[now_node] == 0:
        visited[now_node] = count # 방문 순서 표시
        count += 1 
        for adj_node in adj_list[now_node]: # 주변 노드에 대해
            stack.append(adj_node)
for order in visited[1:]:
    print(order)