def solution(numbers, target):
    count = 0
    stack = []
    stack.append([numbers[0],0])
    stack.append([-numbers[0],0]) # 계산결과, 인덱스
    while stack:
        result, idx = stack.pop()
        if idx < len(numbers) - 1:
            stack.append([result - numbers[idx + 1], idx + 1])
            stack.append([result + numbers[idx + 1], idx + 1])
        else:
            if result == target:
                count += 1
    return count