def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stack = []
    count = [0] 
    answer = [-1]
    def dfs(now_node):
        #print(now_node)
        count[0] += 1
        if now_node == word:
            answer[0] = count[0]
        if len(now_node) < 5:
            for vowel in vowels:
                dfs(now_node + vowel)
    dfs('A')
    dfs('E')
    dfs('I')
    dfs('O')
    dfs('U')
    return answer[0]