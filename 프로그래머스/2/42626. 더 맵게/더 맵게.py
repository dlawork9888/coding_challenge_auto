import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        food_1 = heapq.heappop(scoville)
        food_2 = heapq.heappop(scoville)
        new_scoville = food_1 + (food_2 * 2)
        count += 1
        heapq.heappush(scoville, new_scoville)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return count
