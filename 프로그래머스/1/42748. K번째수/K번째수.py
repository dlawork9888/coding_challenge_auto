def solution(array, commands):
    answer = []
    for command in commands:
        start, end, k = command
        sliced = sorted(array[start-1:end])
        answer.append(sliced[k-1])
    return answer