def solution(arr):
    stack = []
    now_num = None
    for ele in arr:
        if ele != now_num:
            now_num = ele
            stack.append(now_num)
    return stack