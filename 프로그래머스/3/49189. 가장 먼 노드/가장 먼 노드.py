from collections import defaultdict as dd
from collections import deque as dq

def solution(n, edges):
    
    # 인접 리스트, 무방향 그래프
    adj_list = dd(list)
    for edge in edges:
        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)
    
    # 1(0)번 노드에서 가장 멀리 떨어진 노드가 몇개? => BFS, visited는 거리를 저장
    visited = [-1 for _ in range(n)]
    start_node = 0
    q = dq()
    q.append(start_node)
    visited[0] = 0
    while q:
        now_node = q.popleft()
        now_distance = visited[now_node]
        # 인접 노드 탐색
        for node in adj_list[now_node]:
            # 미방문 노드라면
            if visited[node] == -1:
                visited[node] = now_distance + 1
                q.append(node)
    # BFS 완료 => 가장 먼 거리의 노드 개수를 세어보자
    visited.sort(reverse = True)
    max_distance = visited[0]
    count = 0
    for distance in visited:
        if distance == max_distance:
            count += 1
        else: break # 아니면 바로 종료 => 시간 아까움
    
    return count