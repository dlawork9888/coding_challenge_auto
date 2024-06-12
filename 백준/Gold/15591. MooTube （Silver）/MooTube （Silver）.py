# 최종

from collections import defaultdict 
# 입력 처리
def input_process():
    # N, Q
    N, Q = [int(x) for x in input().split()]
    # 인접리스트, 무방향 그래프
    adj_list = defaultdict(list)
    for _ in range(N-1):
        p, q, r = [int(x) for x in input().split()]
        adj_list[p].append((q,r)) # 상대 정점, 가중치
        adj_list[q].append((p,r))
    # 질문
    questions = []
    for _ in range(Q):
        questions.append([int(x) for x in input().split()])
    return N, Q, adj_list, questions

import math
def answer_process(N, adj_list, question):
    k, v = question
    #print(f'가중치가 {k}라면 {v}를 보고 있는 소들은 몇개의 추천을?')
    answer = 0
    # dfs
    start_node = v
    mins = [math.inf for _ in range(N + 1)]
    stack = [start_node]
    mins[start_node] = math.inf
    while stack:
        now_node = stack.pop()
        #print(f'---now_node: {now_node}')
        for adj_node, weight in adj_list[now_node]:
            #print(f'adj_node, weight: {adj_node, weight}')
            if mins[adj_node] != math.inf or adj_node == start_node:
                #print('탐색한 노드')
                continue
            # 탐색 안한 노드라면
            if mins[now_node] > weight:
                mins[adj_node] = weight
            else:
                mins[adj_node] = mins[now_node]
            stack.append(adj_node)
    #print(f'------------mins: {mins}')
    answer = 0
    for x in mins:
        if x != math.inf and x >= k:
            answer += 1
    return answer

N, Q, adj_list, questions = input_process()
for question in questions:
    answer = answer_process(N, adj_list, question)
    print(answer)