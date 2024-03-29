from collections import defaultdict

def is_bipartite_graph(V, E):
    
    # 인접 리스트 생성
    # 이분 그래프는 특성상 무(양)방향
    # 입력이 연결 그래프인가 ... => 연결 그래프라는 보장이 없음(끊어진 그래프) ! DFS 수정!
    adj_list = defaultdict(list)
    for _ in range(E):
        u, v = [int(x)-1 for x in input().split()]
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # DFS로 하자 ! <= import deque 안해도 됨 
    colors = [-1 for _ in range(V)] # -1은 미탐색, 0,1은 탐색 and 색칠
    
    # colors 중에서 어느 하나라도 미탐색이라면
    while any([True if x == -1 else False for x in colors]):
        stack = []
        start_node = -1
        for idx, color in enumerate(colors):
            if color == -1:
                start_node = idx
                break
        stack.append(start_node)
        colors[start_node] = 0 #최초 탐색 노드 0으로 설정

        while stack:
            now_node = stack.pop()
            # 인접 노드에 대해서
            for node in adj_list[now_node]:
                # 미탐색이라면 다른 색으로 칠하고
                if colors[node] == -1:
                    colors[node] = 0 if colors[now_node] == 1 else 1
                    # stack에 추가
                    stack.append(node) 
                else: # 이미 탐색한 노드라면 
                    # 같은 색인지 확인해야지 => 같은 색이라면 이분그래프가 아님!
                    if colors[node] == colors[now_node]:
                        return 'NO'
    return 'YES'

# 입력 처리 
testcase = int(input())
for _ in range(testcase):
    V, E = [int(x) for x in input().split()]
    print(is_bipartite_graph(V, E))