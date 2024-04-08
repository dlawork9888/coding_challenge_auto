from collections import deque as dq

def solution(maps):
    # 경로의 최솟값 => BFS
    # visited는 방문여부만이 아니라, 해당 노드까지의 경로 길이를 기록해야 한다.
    
    # directions
    d_row = [-1, 0, 1, 0]
    d_col = [0, -1, 0, 1]
    # visited 
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # BFS 
    q = dq()
    start_node = [0,0] # 시작 좌표 => [row, col]
    visited[start_node[0]][start_node[0]] = 1 # 방문 표시, 경로값은 1
    q.append(start_node)
    while q:
        now_node = q.popleft()
        # 다음 노드 탐색
        for i in range(4):
            next_row = now_node[0] + d_row[i]
            next_col = now_node[1] + d_col[i]
            # 1. 좌표가 맵 안에 있나?
            # 2. 갈 수 있는 노드인가? (벽이 아닌가?) => 갈 수 있다면, 미방문인가?
            if 0 <= next_row < len(maps) and 0 <= next_col < len(maps[0]): 
                if maps[next_row][next_col] != 0 and visited[next_row][next_col] == -1:
                    # 그러면 방문 표시(현재 노드의 경로값 + 1)하고 큐에 넣자
                    visited[next_row][next_col] = visited[now_node[0]][now_node[1]] + 1
                    q.append([next_row, next_col])
    return visited[-1][-1]
        
        
    