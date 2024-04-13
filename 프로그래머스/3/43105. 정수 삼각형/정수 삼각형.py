def solution(triangle):
    for floor in range(len(triangle) - 2, -1, -1):
        for idx, ele in enumerate(triangle[floor]):
            triangle[floor][idx] += triangle[floor + 1][idx] if triangle[floor + 1][idx] > triangle[floor + 1][idx + 1] else triangle[floor + 1][idx + 1]
    return triangle[0][0]
            