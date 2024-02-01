def solution(number, k):
    stack = []
    count = 0
    for x in number:
        x = int(x)
        # 스택이 비었거나 Top이 더 크거나 같다면
        # 일단 먹기
        if not stack or stack[-1] >= x:
            stack.append(x)
            continue
        while stack and stack[-1] < x and count < k:
            stack.pop()
            count += 1
        stack.append(x)
    if len(stack) > len(number) - k:
        return ''.join(map(str,stack))[:-k]
    else:
        return ''.join(map(str,stack))