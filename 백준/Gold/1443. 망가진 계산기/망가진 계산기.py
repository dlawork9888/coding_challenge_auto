# DP ?

D, P = [int(x) for x in input().split()]

dp = [1]
multiply = range(2,10)

for p in range(P): # 0,1,2
    dp_next = []
    for e in dp:
        for m in multiply:
            if len(str(e*m)) > D:
                continue
            dp_next.append(e*m)
    dp_next = list(set(dp_next))
    dp = dp_next

dp.sort(key = lambda x: -x)

flag = False
for e in dp:
    if len(str(e)) <= D:
        print(e)
        flag = True
        break
if flag == False:
    print(-1)