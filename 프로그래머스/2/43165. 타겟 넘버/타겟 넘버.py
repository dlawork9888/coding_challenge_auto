# recursive DFS를 써보자 !

def solution(numbers, target):
    count = [0]

    start_node = [0, 0] # 다음에 더하거나 뺄 원소의 인덱스, calculation result

    def dfs_recursive(node):
        if node[0] == len(numbers):
            if node[1] == target:
                count[0] += 1
        else: # 다음 재귀
            
            now_index = node[0]
            next_index = node[0] + 1
            result = node[1]
            
            dfs_recursive([next_index, result + numbers[now_index]])
            dfs_recursive([next_index, result - numbers[now_index]])
            
        return
    
    dfs_recursive(start_node)
    
    return count[0]
    