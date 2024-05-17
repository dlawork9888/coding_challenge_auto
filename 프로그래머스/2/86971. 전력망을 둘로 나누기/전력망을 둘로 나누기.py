# Disjoint Set도 괜찮을듯
# 간선 하나 없애고 그걸로 인접리스트 만들기
# => 해당 그래프를 탐색하며 노드 새기
# => 모든 노드를 탐색할 때까지
from collections import defaultdict, deque

# 간선 하나 없어진 wires가 인자로
def make_adj_list_and_search(n, wires):
    # 인접 리스트 생성
    adj_list = defaultdict(list)
    # 노드는 1번부터 시작임 => -1을 해주자
    for node1, node2 in wires:
        adj_list[node1 - 1].append(node2 - 1)
        adj_list[node2 - 1].append(node1 - 1)
    
    visited = [False for _ in range(n)]
    counts = []
    while all(visited) == False:
        count = 0
        start_node = -1
        for idx, visited_value in enumerate(visited):
            if visited_value == False: 
                start_node = idx
                break
        q = deque()
        q.append(start_node)
        visited[start_node] = True
        while q:
            now_node = q.pop() #DFS
            count += 1
            # 주위 노드 탐색
            for node in adj_list[now_node]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True
        counts.append(count)
    #print(f'counts:{counts}')
    return abs(counts[0] - counts[1])
    
def solution(n, wires):
    diffs = []
    for idx, wire in enumerate(wires):
        diff = make_adj_list_and_search(n, wires[0:idx] + wires[idx + 1:])
        diffs.append(diff)
    return min(diffs)
    
