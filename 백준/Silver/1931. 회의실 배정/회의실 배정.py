# 최종
N = int(input())

def input_process(N):
    meetings = []
    for _ in range(N):
        meeting = [int(x) for x in input().split()]
        meetings.append(meeting)
    return meetings

meetings = input_process(N)
meetings.sort(key = lambda x: (x[1],x[0]))

count = 0
finish_time = 0
for meeting in meetings:
    if meeting[0] >= finish_time:
        count += 1
        finish_time = meeting[1]
print(count)