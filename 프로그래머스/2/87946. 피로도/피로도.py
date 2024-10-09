# recursive dfs

def solution(k, dungeons):
    max_depth = [-1]
    
    def dfs(node, k, visited):
        now_visited = visited[:]
        # 방문 -> 방문 체크, 체력 소모
        now_visited[node] = True
        now_k = k - dungeons[node][1]
        # max_depth 체크
        count = 0
        for is_visited in now_visited:
            if is_visited == True:
                count += 1
        if count > max_depth[0]:
            max_depth[0] = count
        for next_node in range(len(dungeons)):
            # 방문할 수 있는 노드를 방문하자
            if now_visited[next_node] == False and now_k >= dungeons[next_node][0]:
                dfs(next_node, now_k, now_visited)
    # start_node, k, visited
    for node, dungeon in enumerate(dungeons):
        if k >= dungeon[0]: 
            dfs(node, k, [False for _ in range(len(dungeons))])
    return max_depth[0]