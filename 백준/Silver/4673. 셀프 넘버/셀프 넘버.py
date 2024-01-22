# 테스트 완료
# 통합 풀이
def d(n):
    # 각 자리 수 산출
    str_n = str(n)
    for x in str_n:
        n += int(x)
    return n

arr = [True] * 10001

# 각 숫자들로 만든 수를 False 처리
for i, bool in enumerate(arr):
    if d(i) <= 10000:
        arr[d(i)] = False

for idx, x in enumerate(arr):
    if x == True:
        print(idx)