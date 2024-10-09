def solution(n, times):
    times.sort()
    max_time = times[-1]*n
    min_time = times[0]
    
    while min_time <= max_time:
        mid_time = (max_time + min_time)//2
        hm_mans = 0
        for time in times:
            hm_mans += mid_time//time
        #print(f'hm_mans: {hm_mans}')
        if hm_mans >= n:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
    
    return min_time