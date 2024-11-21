# 통합

## 입력 처리
n_stair = int(input())
scores = []
for _ in range(n_stair):
    scores.append(int(input()))
    
dp = []
for i in range(n_stair):
    if i == 0:
        dp.append([0, scores[0]])
        continue
    if i == 1:
        dp.append([scores[1], scores[0]+scores[1]])
        continue
    # 전 계단에서 올라온 것
    from_before = dp[i-1][0] + scores[i]
    # 전전 계단에서 올라온 것
    from_bebefore = max([dp[i-2][1] + scores[i], dp[i-2][0] + scores[i]])
    dp.append([from_bebefore, from_before])
    
print(max(dp[-1]))