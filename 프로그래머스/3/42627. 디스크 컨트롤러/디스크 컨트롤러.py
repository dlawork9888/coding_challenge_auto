import heapq

def solution(jobs):
    n_jobs = len(jobs)
    jobs.sort(key = lambda x: -x[0])
    min_heap = []
    now_time = 0
    full_time_sum = 0
    while jobs or min_heap:
        # 작업 안하고 힙에 job이 없을때 -> 바로 실행
        if not min_heap and now_time <= jobs[-1][0]:
            start, job_time = jobs.pop()
            now_time = start + job_time
            full_time_sum += job_time
            continue
        # 작업 힙에 넣기
        while jobs and now_time > jobs[-1][0]:
            job = jobs.pop()
            heapq.heappush(min_heap, (job[1], job[0]))
        # 작업 하나 실행
        job_time, start = heapq.heappop(min_heap)
        now_time += job_time
        full_time_sum += now_time - start
        
    return full_time_sum//n_jobs