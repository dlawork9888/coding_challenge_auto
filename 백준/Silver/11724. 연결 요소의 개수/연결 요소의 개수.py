from collections import defaultdict

# # 예제 입력
# N, M = 6, 5
# edges = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]
# adj_list = defaultdict(list)
# for [u, v] in edges:
#     adj_list[u-1].append(v-1)
#     adj_list[v-1].append(u-1)
# #print(f"adj_list: {adj_list}")
    
#### 입력 처리

# 첫째줄 
# 정점의 개수 N
# 간선의 개수 M
N, M = [int(x) for x in input().split()]

# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v
# 연결리스트 사용
adj_list = defaultdict(list)
for _ in range(M):
    u, v = [int(x) for x in input().split()]
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

# visited 배열 정의
visited = [False for x in range(N)]
#print(f"visited 정의: {visited}")
connected = 0

# dfs
for start_node in range(N):
    if not visited[start_node]:
        stack = [start_node]
        visited[start_node] = True
        
        while stack:
            now_node = stack.pop()
            for adj_node in adj_list[now_node]:
                if not visited[adj_node]:
                    stack.append(adj_node)
                    visited[adj_node] = True
        
        connected += 1

print(connected)