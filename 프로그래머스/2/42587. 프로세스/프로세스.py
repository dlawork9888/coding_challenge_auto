from collections import deque

def solution(priorities, location):
    waiting_queue = deque()
    for idx, priority in enumerate(priorities):
        if idx == location:
            waiting_queue.append((priority, True))
        else:
            waiting_queue.append((priority, False))
    
    count = 0
    while waiting_queue:
        now_priority, target = waiting_queue.popleft()
        execute_flag = True
        # 우선 순위가 큰게 있는지 검사
        for priority,_ in waiting_queue:
            if priority > now_priority:
                execute_flag = False
                break
        # 큰게 있으면
        if execute_flag == False:
            waiting_queue.append((now_priority, target))
            continue
        # 큰게 없으면 -> 실행
        else:
            count += 1
            if target:
                break
    return count