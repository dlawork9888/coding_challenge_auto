# 입력 처리
computers = int(input())
connections = int(input())

# 인접 행렬 생성
# 사실 인접 행렬보다 인접 리스트가 더 나을 것 같긴함
# 128MB, 컴퓨터 100개 제한 => 인접행렬: 4 bytes * 100 * 100 = 40000 bytes => 40KB
adj_mat = [[0 for _ in range(computers)] for _ in range(computers)]
for _ in range(connections):
    connection = [int(x) - 1 for x in input().split()] # [1,2] => [0,1]
    # print(connection)
    # 인접 행렬에 연결 표시
    adj_mat[connection[0]][connection[1]] = 1
    adj_mat[connection[1]][connection[0]] = 1

##### 
##### BFS
#####

from collections import deque

# 연결된 컴퓨터 수 카운트
count = 0

# 큐 , visited 준비
queue = deque()
start_node = 0
queue.append(start_node)
visited = [False for _ in range(computers)]
visited[start_node] = True

# 탐색 시작 !
while queue: # 큐가 차있을 동안
    now_node = queue.popleft()
    # 연결된 노드 탐색
    for idx, connected in enumerate(adj_mat[now_node]):
        if visited[idx] == False and connected == 1: # 방문한 적 없고 연결되어있다 ?
            # 큐에 추가
            queue.append(idx)
            count += 1
            # 방문 표시
            visited[idx] = True

# sol !
print(count)