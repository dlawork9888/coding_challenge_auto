# COUNT_0 = 0
# COUNT_1 = 0

# def fibonacci(N):
#     global COUNT_0
#     global COUNT_1
#     if N == 0: 
#         COUNT_0 += 1
#         return 0
#     if N == 1: 
#         COUNT_1 += 1
#         return 1
#     return fibonacci(N-1) + fibonacci(N-2)

# # 압력 
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     fibonacci(N)
#     print(COUNT_0, COUNT_1)
#     COUNT_0 = 0
#     COUNT_1 = 0

# => 정답은 맞는 것 같은데 시간초과
# DP 활용

dp_table = [[-1,-1] for x in range(41)]

# fibonacci(40)은 fibonacci(39) fibonacci(38)을 호출
# [COUNT_0, COUNT_1] => fibonacci(0): [1, 0], fibonacci(1):[0, 1], fibonacci(2): [1, 1]
# fibonacci(3) =  fibonacci(2) + fibonacci(1) = fibonacci(1) + fibonacci(1) + fibonacci(0) => [1, 2]

dp_table[0] = [1, 0]
dp_table[1] = [0, 1]

def fibonacci_bin(N):
    if N == 0:
        return dp_table[0]
    if N == 1:
        return dp_table[1]
    if dp_table[N] != [-1 , -1]:
        return dp_table[N]
    dp_table[N] = [x+y for x,y in zip(fibonacci_bin(N-1), fibonacci_bin(N-2))]
    return dp_table[N]

T = int(input())
for _ in range(T):
    x, y = fibonacci_bin(int(input()))
    print(f"{x} {y}")