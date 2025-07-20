# IMPORT 
from collections import defaultdict
import heapq
import math
# 첫쨰줄에 학생수 N, 간선의 개수 M, 파티가 열리는 마을 X
# 도로의 시작 노드, 끝 노드, 가중치
# 예제 입력
# line_0 = "4 8 2"
# lines = [
#     "1 2 4",
#     "1 3 2",
#     "1 4 7",
#     "2 1 1",
#     "2 3 5",
#     "3 1 2",
#     "3 4 4",
#     "4 2 3"
# ]

# 입력 처리
line_0 = input()
N, M, X = [int(x) for x in line_0.split()]
X = X - 1  # X를 0부터 시작하는 인덱스로 변환
lines = []
for _ in range(M):
    lines.append(input())
adj_list = defaultdict(list)
# 시작노드: [[끝노드, 가중치], ]
# 노드는 0부터 시작하는걸로
for line in lines:
    start_node, end_node, weight = [int(x) for x in line.split()]
    start_node += -1
    end_node += -1  
    adj_list[start_node].append((end_node, weight))
#print(f"adj_list: {adj_list}")

# 각 학생이 오고 가는데 가장 짧은 거리
# = 각 노드의 최단 사이클 -> 다익스트라
# 각 노드에서 X까지의 최단 거리 + X에서 각 노드까지의 최단 거리

def dijkstra(start_node):
    visited = [False for _ in range(N)]
    min_dist = [math.inf for _ in range(N)]
    heap = []
    heapq.heappush(heap, (0, start_node))
    min_dist[start_node] = 0
    while heap:
        #print(f"heap: {heap}")
        weight, now_node = heapq.heappop(heap)
        #print(f"now_node: {now_node}")
        if visited[now_node] == True:
            continue
        visited[now_node] = True
        for adj_node, weight in adj_list[now_node]:
            if min_dist[now_node] + weight < min_dist[adj_node]:
                min_dist[adj_node] = min_dist[now_node] + weight
                heapq.heappush(heap, (min_dist[adj_node], adj_node))
    #print(f"{start_node}부터 모든 노드까지의 최소거리: {min_dist}")
    return min_dist

min_dists_to_X = []
for start_node in range(N):
    #print(f"===={start_node}부터 X까지의 최소 거리====")
    min_dists = dijkstra(start_node)
    min_dists_to_X.append(min_dists[X])

#print(f"min_dists_to_X: {min_dists_to_X}")
min_dists_to_all_nodes = dijkstra(X)
#print(f"min_dists_to_all_nodes: {min_dists_to_all_nodes}")
print(max([x+y for x,y in zip(min_dists_to_X, min_dists_to_all_nodes)]))