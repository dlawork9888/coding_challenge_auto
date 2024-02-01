from collections import deque

def solution(n, computers): # 컴퓨터 수, 인접 행렬
    visited = [False for _ in range(n)]
    
    
    def find_start_node():
        # 시작 노드 탐색
        start_node = -1
        for node, is_visited in enumerate(visited):
            if is_visited == False: # 미방문 노드?
                start_node = node
                break
        return start_node



    def dfs_stack(start_node):
        # 시작 노드 스택에 넣고 방문 처리
        # 스택이 차있을 동안 반복(= 더 이상 탐색이 불가능할 때까지)
            # 스택에서 빼기
            # 미방문 인접 노드 조사
            # 스택에 넣고 방문 표시
        stack = deque()
        # 시작 노드를 스택에 넣고 방문 처리
        stack.append(start_node)
        visited[start_node] = True
        # 스택이 차있을 동안 
        while stack:
            # 스택에서 빼기
            now_node = stack.pop()
            # 미방문 인접 노드 조사
            for adj_node, is_wired in enumerate(computers[now_node]):
                if visited[adj_node] == False and is_wired == 1:
                    # 스택에 넣고 방문 표시
                    stack.append(adj_node)
                    visited[adj_node] = True
    
    
    
    def dfs_recursive(node):
        # 미방문 인접노드에 대해여 재귀 실행
        for adj_node, is_wired in enumerate(computers[node]):
            if visited[adj_node] == False and is_wired == 1:
                visited[adj_node] = True
                dfs_recursive(adj_node)


    def bfs(start_node):
        # 시작노드 방문 처리
        visited[start_node] = True
        # 큐에 넣기 
        dq = deque()
        dq.append(start_node)
        # 큐가 차있는 동안 반복
        while dq:
            now_node = dq.popleft()
            # 미방문 인접 노드 조사
            for adj_node, is_wired in enumerate(computers[now_node]):
                if visited[adj_node] == False and is_wired == 1:
                    # 큐에 넣고 방문 표시
                    dq.append(adj_node)
                    visited[adj_node] = True
                
    count = 0
    while not all(visited): # 전부 방문은 아닐 동안 => 전부 방문할 때까지
        
        start_node = find_start_node()
        
        
        # dfs_stack
        #dfs_stack(start_node)
        
        # dfs_recursive
        #visited[start_node] = True
        #dfs_recursive(start_node)

        # bfs
        bfs(start_node)
        count += 1
        
    return count 