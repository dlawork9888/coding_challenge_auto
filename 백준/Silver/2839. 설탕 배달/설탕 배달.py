# 5x + 3y = N
# (x,y) 중 x가 제일 큰 쌍
def bags(N):
    for x in range(N//5, -1, -1):
        if (N - 5*x) % 3 == 0:
            return x + (N - 5*x)//3
    return -1
print(bags(int(input())))