import heapq
from collections import defaultdict

def op_prcs(op): 
    op = op.split()
    op[1] = int(op[1])
    return op

def solution(operations):
    ### CUSTOM TESTCASE
    #operations = ['I 1', 'I 2', 'I 3','I 4' , 'D 1', 'D -1', 'I 1', 'I 3', 'D 1']
    
    min_heap = []
    max_heap = []
    check = defaultdict(int)
    
    # operation 처리
    for op in operations:
        op = op_prcs(op)

        # Insert operation
        if op[0] == 'I':
            heapq.heappush( min_heap, op[1] )
            heapq.heappush( max_heap, -op[1] )
            check[op[1]] += 1

        # Delete Operation
        else:
            if op[-1] == -1:
                while min_heap: # Min Delete
                    # 존재하는 값인지 확인
                    est_min = min_heap[0]
                    # 존재한다면
                    if check[est_min] > 0:
                        check[est_min] -= 1
                        heapq.heappop(min_heap)
                        break
                    # 존재하지 않는다면
                    else:
                        heapq.heappop(min_heap)
                        
            else: 
                while max_heap: # Max Delete
                    est_max = -max_heap[0]
                    if check[est_max] > 0:
                        check[est_max] -= 1
                        heapq.heappop(max_heap)
                        break
                    else:
                        heapq.heappop(max_heap)
    ### FOR DEBUGGING
    #print(f'min_heap: {min_heap}')
    #print(f'max_heap: {max_heap}')
    #print(f'check: {check}')
    
    answer = []
    while max_heap:
        est_max = -max_heap[0]
        if check[est_max] > 0:
            answer.append(est_max)
            break
        else:
            heapq.heappop(max_heap)
    while min_heap:
        est_min = min_heap[0]
        if check[est_min] > 0:
            answer.append(est_min)
            break
        else:
            heapq.heappop(min_heap)
    
    return answer if answer else [0, 0]