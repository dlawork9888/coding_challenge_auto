from collections import defaultdict

def solution(tickets):
    # 인접 리스트
    adj_list = defaultdict(list)
    edges = defaultdict(list)
    for start, end in tickets:
        adj_list[start].append(end)
    
    # 인접 리스트 정렬 및 간선 방문 여부 초기화
    for key in adj_list:
        adj_list[key].sort()
        edges[key] = [False for _ in range(len(adj_list[key]))]
    
    #print(f'adj_list: {adj_list}')
    #print(f'edges: {edges}')
    
    answer = []

    def dfs(departure, route):
        nonlocal answer
        if len(route) == len(tickets) + 1:
            answer = route
            return True
        
        for idx, arrival in enumerate(adj_list[departure]):
            if not edges[departure][idx]:
                edges[departure][idx] = True
                if dfs(arrival, route + [arrival]):
                    return True
                edges[departure][idx] = False  # 재귀에서 돌아오면 다시 돌려놓기
    
        return False

    dfs('ICN', ['ICN'])
    return answer
