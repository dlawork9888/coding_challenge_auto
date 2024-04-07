import sys
sys.setrecursionlimit(100000)

# 새로운 시작
def sol():
    V = int(input())
    adj_arr = [int(x)-1 for x in input().split()]
    visited = [False for _ in range(V)]
    global team
    team = 0
    path = []
    def dfs_recursive(node):
        global team
        visited[node] = True
        #print(f'now_node: {node}')
        next_node = adj_arr[node]
        #print(f'next_node: {next_node}')
        path.append(node)
        if visited[next_node] == True:
            if next_node in path:
                #print(f'path: {path}')
                team += len(path) - path.index(next_node)
        else:
            dfs_recursive(next_node)

    for x in range(V):
        if visited[x] != True:
            path = []
            dfs_recursive(x)
            
    return V - team

for _ in range(int(input())):
    print(sol())