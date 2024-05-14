from collections import defaultdict
import heapq

def prim():
    vertex_num, edge_num = [int(x) for x in input().split()]
    adj_list = defaultdict(list)
    for _ in range(edge_num):
        u, v, weight = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))
    #print(f'adj_list: {adj_list}')
    mst = []
    visited = [False for _ in range(vertex_num)]
    min_heap = [(0,0)] # (가중치, 시작 노드), 0번 노드 추가
    while min_heap:
        #print(f'min_heap: {min_heap}')
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append((u, weight))
        for next_weight, v in adj_list[u]:
            if visited[v] == False:
                heapq.heappush(min_heap, (next_weight, v))
    #print(f'mst: {mst}')
    weight_sum = 0
    for _, weight in mst:
        weight_sum += weight

    return weight_sum

for testcase in range(1, int(input()) + 1):
    print(f'#{testcase} {prim()}')