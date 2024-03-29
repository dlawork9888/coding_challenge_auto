
# 입력 처리
N, M = [int(x) for x in input().split()]

# 인접 리스트
from collections import defaultdict
adj_list = defaultdict(list)
for _ in range(M):
    u, v = [int(x)-1 for x in input().split()]
    adj_list[u].append(v)
    
# 위상 정렬
# Kahn

# 진입 차수 계산
indgrees = [0 for _ in range(N)]
for key, value in adj_list.items():
    for ele in value:
        indgrees[ele] += 1

from collections import deque as dq
q = dq()
for idx, indgree in enumerate(indgrees):
    if indgree == 0:
        q.append(idx)
        indgrees[idx] = -1
        

topology_sort_result = []
while q:
    now_node = q.popleft()
    topology_sort_result.append(now_node)
    for node in adj_list[now_node]: # 인접노드들 진입차수 1감소
        indgrees[node] -= 1
    del adj_list[now_node]
    for idx, indgree in enumerate(indgrees):
        if indgree == 0:
            q.append(idx)
            indgrees[idx] = -1
# 출력           
print(" ".join([str(x+1) for x in topology_sort_result]))