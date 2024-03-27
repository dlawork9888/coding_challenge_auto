# 입력 처리
N = int(input())

# 인접 리스트
from collections import defaultdict
adj_list = defaultdict(list)
for _ in range(N - 1):
    edge = [int(x)-1 for x in input().split()]
    # 우선 무방향 그래프로
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
    
# 부모 체크 배열 생성
parents = [-1 for _ in range(N)]
parents[0] = -2 # 루트 부모는 -2로 표시해서 방문체크까지 한번에 !
# BFS
from collections import deque
queue = deque()
start_node = 0
queue.append(start_node)
while queue:
    now_node = queue.pop()
    # 연결 노드들에 대하여 부모 표시
    for node in adj_list[now_node]:
        # 부모 표시가 안된 노드(미방문)면 큐에 추가하고 부모 표시
        if parents[node] == -1:
            parents[node] = now_node
            queue.append(node)
for parent in parents[1:]:
    print(parent+1)