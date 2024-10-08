import math

def solution(progresses, speeds):
    remains = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds) ]
    
    ref_val = -1
    count = 0
    answer = []
    for remain in remains:
        if ref_val == -1:
            ref_val = remain
            count += 1
            continue
        if ref_val < remain:
            answer.append(count)
            ref_val = remain
            count = 1
            continue
        count += 1
    answer.append(count)
    
    return answer