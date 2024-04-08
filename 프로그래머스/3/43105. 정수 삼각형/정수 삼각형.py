# 또 풀기

def solution(triangle):
    # Top - Down
    # 따로 메모이제이션 리스트를 두지 말자
    # 바로 경로값을 갱신하자 !
    for floor, vals in enumerate(triangle):
        # 0층은 아무것도 하지 않는다
        if floor == 0:
            continue
        # 층 접근
        for idx, val in enumerate(vals):
            # 맨 앞
            if idx == 0:
                vals[idx] += triangle[floor - 1][0]
            # 맨 뒤
            elif idx == floor:
                vals[idx] += triangle[floor - 1][floor - 1]
            # 가운데
            else:
                if triangle[floor - 1][idx - 1] < triangle[floor - 1][idx]:
                    vals[idx] += triangle[floor - 1][idx]
                else:
                    vals[idx] += triangle[floor - 1][idx - 1]
    triangle[-1].sort()
    return triangle[-1][-1]