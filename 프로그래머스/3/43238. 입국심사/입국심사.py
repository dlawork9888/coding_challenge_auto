

def solution(n, times):

    times.sort()
    min_time = 0
    max_time = times[-1]
    
    start_time = min_time * n
    end_time = max_time * n
    
    
    def full(now_time):
        count = 0
        for time in times:
            count += now_time//time
        return count
    
    
    while start_time < end_time:
        mid_time = (start_time + end_time)//2 
        if full(mid_time) >= n: # 시간 너무 많이 줬다
            end_time = mid_time
        else: # 시간 너무 적게 줬다
            start_time = mid_time + 1
            
    return start_time
             